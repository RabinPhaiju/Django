# Generated by Django 5.1.1 on 2024-10-05 03:24

import django.core.files.storage
import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=pathlib.PurePosixPath('/mnt/backup/Projects/Django/django5learn/media/photos')), upload_to=''),
        ),
    ]