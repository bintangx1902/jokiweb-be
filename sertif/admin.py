from django.contrib.admin import site
from .models import *

site.register(UploadedFile)
site.register(CertificateType)
