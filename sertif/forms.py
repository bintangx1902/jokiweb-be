from django import forms
from .models import *


class UploadFileForms(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = '__all__'
