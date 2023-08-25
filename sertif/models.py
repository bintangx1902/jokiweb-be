from django.db import models
import os
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


class CertificateType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Certification(models.Model):
    full_name = models.CharField(max_length=255)
    batch = models.CharField(max_length=255)
    no_participant = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    type_certification = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_name} - {self.no_participant}"


class LecturerCertification(models.Model):
    full_name = models.CharField(max_length=255)
    program = models.CharField(max_length=255)
    batch = models.CharField(max_length=255)
    no_participant = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    is_lecturer = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.full_name} - {self.program}"


class MikroTikCertification(models.Model):
    full_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_name} - {self.status}"
