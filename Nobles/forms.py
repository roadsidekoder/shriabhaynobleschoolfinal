from django import forms
from django.forms.models import BaseInlineFormSet
from tinymce import TinyMCE
from .models import Notice


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class NoticeForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Notice
        fields = '__all__'


class AtLeastOneRequiredInlineFormSet(BaseInlineFormSet):

    def clean(self):
        """Check that at least one service has been entered."""
        super(AtLeastOneRequiredInlineFormSet, self).clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False)
            for cleaned_data in self.cleaned_data):
            raise forms.ValidationError('At least one image required.')