# Generated by Django 3.2.18 on 2023-06-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sertif', '0012_rename_mikrotikcertification_lecturercertification'),
    ]

    operations = [
        migrations.CreateModel(
            name='MikroTikCertification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]
