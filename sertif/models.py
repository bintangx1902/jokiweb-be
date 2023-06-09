from django.db import models
import os
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


class CertificateType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class UploadedFile(models.Model):
    full_name = models.CharField(max_length=255)
    nim = models.CharField(max_length=255)
    prodi = models.CharField(max_length=255)
    type = models.ForeignKey(CertificateType, on_delete=models.CASCADE)
    file = models.FileField(upload_to='file/')
    nidn = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nim} - {self.type} - {self.filename()}"

    def filename(self):
        return os.path.basename(self.file.name)

    def delete(self, using=None, *args, **kwargs):
        try:
            file_path = os.path.join(settings.MEDIA_ROOT, self.file.name)
            if os.path.isfile(file_path):
                os.remove(file_path)
        except ObjectDoesNotExist as e:
            print("file does not exist!")

        return super().delete(*args, **kwargs)

    def date(self):
        return self.upload_date.strftime("%d - %m - %y : %h:%m")
