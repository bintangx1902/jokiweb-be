from django import forms
from .models import *


class UploadFileForms(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'
