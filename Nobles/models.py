from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from tinymce import HTMLField
from django.utils import timezone
# Create your models here.

class Gallery(models.Model):
    title = models.CharField('Title', max_length=20)
    cover_photo = models.ImageField(upload_to='images/', null=True)
    event_date = models.DateField()
    last_update = models.DateField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    cover_photo_thumbnail = ImageSpecField(source='cover_photo',
                                      processors=[ResizeToFill(400, 270)],
                                      format='JPEG',
                                      options={'quality': 50})

    def __str__(self):
        return self.title

    class Meta:
         verbose_name_plural = "Gallery"


class Image(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.CASCADE)
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(400, 270)],
                                      format='JPEG',
                                      options={'quality': 100})
    image_size = ImageSpecField(source='image',
                                      format='JPEG',
                                      options={'quality': 30})

    def delete_image_kit_image_field(image_kit_field):
    # ImageKit has a bug where files are cached and not deleted right away
    # https://github.com/matthewwithanm/django-imagekit/issues/229#issuecomment-315690575

        if not image_kit_field:
            return

        try:
            file = image_kit_field.file
        except FileNotFoundError:
            pass
        else:
            cache = get_cache()
            cache.delete(cache.get(file))
            image_kit_field.storage.delete(file.name)

        image_kit_field.delete()

    def __str__(self):
        return str(self.image)  

class Qualification(models.Model):
    qualification = models.CharField(max_length=50)

    def __str__(self):
        return self.qualification

    class Meta:
         verbose_name_plural = "Qualification"
         ordering = ('qualification',)



class Faculty(models.Model):
    name = models.CharField(max_length=100)
    qualification = models.ManyToManyField(Qualification)
    post = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(200, 270)],
                                      format='JPEG',
                                      options={'quality': 80})

    def __str__(self):
        return self.name
    
    class Meta:
         verbose_name_plural = "Faculty"
         ordering = ('name',)

    

class Notice(models.Model):
    title = models.CharField(max_length=350)
    last_updated = models.DateField(auto_now=True)
    content = HTMLField('Content')

    def __str__(self):
        return self.title


    class Meta:
         verbose_name_plural = "Notice"
         ordering = ['last_updated']

class Infrastructure_and_Facilities(models.Model):
    image = models.ImageField(upload_to='images/')
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(400, 270)],
                                      format='JPEG',
                                      options={'quality': 100})
    image_size = ImageSpecField(source='image',
                                      format='JPEG',
                                      options={'quality': 80})

    def delete_image_kit_image_field(image_kit_field):
    # ImageKit has a bug where files are cached and not deleted right away
    # https://github.com/matthewwithanm/django-imagekit/issues/229#issuecomment-315690575

        if not image_kit_field:
            return

        try:
            file = image_kit_field.file
        except FileNotFoundError:
            pass
        else:
            cache = get_cache()
            cache.delete(cache.get(file))
            image_kit_field.storage.delete(file.name)

        image_kit_field.delete()

    def __str__(self):
        return str(self.image)
    
    class Meta:
         verbose_name_plural = "Infrastructure and Facilities"

class Achievements(models.Model):
    event_title = models.CharField(max_length=200)
    cover_photo = models.ImageField(upload_to='images/')
    image_thumbnail = ImageSpecField(source='cover_photo',
                                      processors=[ResizeToFill(400, 270)],
                                      format='JPEG',
                                      options={'quality': 100})

    cover_photo_toosmall = ImageSpecField(source='cover_photo',
                                      processors=[ResizeToFill(100, 60)],
                                      format='JPEG',
                                      options={'quality': 30})

    event_date = models.DateField()
    event_venue = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.event_title
    
    class Meta:
         verbose_name_plural = "Achievements"
        

class Download(models.Model):
    name = models.CharField(max_length=200)
    your_file = models.FileField(upload_to='files/')
    created_date = models.DateTimeField('date created', default=timezone.now)
    def __str__(self):
        return self.name

class Student(models.Model):
    classroom = models.CharField(max_length=100)

    def __str__(self):
        return self.classroom
    class Meta:
        ordering = ['id']
        verbose_name_plural = "Classroom"

class Homeworks(models.Model):    
    name = models.CharField(max_length=200)
    your_file = models.FileField(upload_to='files/')
    description = models.TextField(blank=True, null=True)
    student = models.ForeignKey('Student',on_delete=models.CASCADE) 
    added = models.DateTimeField('date created', default=timezone.now)
    def __str__(self):
        return self.name

    class Meta:
         verbose_name_plural = "Homeworks"
         ordering = ['added']
    

class Toppers(models.Model):
    name = models.CharField(max_length=200)
    student = models.ForeignKey('Student',on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    photo = models.ImageField(upload_to='images/')
    image_thumbnail = ImageSpecField(source='photo',
                                      processors=[ResizeToFill(190, 225)],
                                      format='JPEG',
                                      options={'quality': 100})

    def __str__(self):
        return self.name
    
    class Meta:
         verbose_name_plural = "Toppers"
        
