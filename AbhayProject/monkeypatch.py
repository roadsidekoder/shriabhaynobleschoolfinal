import logging


LOG = logging.getLogger(__name__)


def PATCH_IMAGEKIT_IMAGECACHEFILE_GENERATE():
    """
    Only needed until this issue gets fixed.
    <https://github.com/matthewwithanm/django-imagekit/issues/391>

    """
    from imagekit.cachefiles import ImageCacheFile
    from imagekit.utils import generate
    from django.core.files import File
    from imagekit.utils import get_logger

    def PATCHED_GENERATE(self):
        # Generate the file
        content = generate(self.generator)

        # PATCHED
        def PATCHED_CLOSE():
            """Protect file from being closed"""
            LOG.warning('patched close() called - ignoring', stack_info=False)

        ORIG_CLOSE = content.close
        content.close = PATCHED_CLOSE

        # Here content.close() gets called which is what we don't want
        actual_name = self.storage.save(self.name, content)

        # restore
        content.close = ORIG_CLOSE
        # /PATCHED

        # We're going to reuse the generated file, so we need to reset the pointer.

        content.seek(0)

        # Store the generated file. If we don't do this, the next time the
        # "file" attribute is accessed, it will result in a call to the storage
        # backend (in ``BaseIKFile._get_file``). Since we already have the
        # contents of the file, what would the point of that be?
        self.file = File(content)

        if actual_name != self.name:
            get_logger().warning(
                'The storage backend %s did not save the file with the'
                ' requested name ("%s") and instead used "%s". This may be'
                ' because a file already existed with the requested name. If'
                ' so, you may have meant to call generate() instead of'
                ' generate(force=True), or there may be a race condition in the'
                ' file backend %s. The saved file will not be used.' % (
                    self.storage,
                    self.name, actual_name,
                    self.cachefile_backend
                )
            )

    # Apply main patch
    LOG.warning('PATCHING ImageCacheFile._generate from imagekit')
    ImageCacheFile._generate = PATCHED_GENERATE


PATCH_IMAGEKIT_IMAGECACHEFILE_GENERATE()