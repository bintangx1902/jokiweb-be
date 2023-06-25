from django.contrib.admin import site
from .models import *

site.register(Certification)
site.register(CertificateType)
site.register(LecturerCertification)
site.register(MikroTikCertification)
