# Generated by Django 3.2.18 on 2023-06-11 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sertif', '0003_uploadedfile_prodi'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]