# Generated by Django 3.2.18 on 2023-06-15 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sertif', '0006_uploadedfile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UploadedFile',
            new_name='Certification',
        ),
    ]