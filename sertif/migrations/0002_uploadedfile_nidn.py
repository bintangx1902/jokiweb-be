# Generated by Django 3.2.18 on 2023-06-06 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sertif', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='nidn',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
