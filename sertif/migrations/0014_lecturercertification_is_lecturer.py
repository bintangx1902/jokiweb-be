# Generated by Django 3.2.19 on 2023-08-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sertif', '0013_mikrotikcertification'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturercertification',
            name='is_lecturer',
            field=models.BooleanField(default=True),
        ),
    ]
