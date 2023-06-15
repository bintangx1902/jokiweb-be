from django.contrib.admin import site
from .models import *

site.register(Certification)
site.register(CertificateType)
