# Generated by Django 3.2.18 on 2023-06-15 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sertif', '0007_rename_uploadedfile_certification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certification',
            old_name='f_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='certification',
            name='l_name',
        ),
    ]