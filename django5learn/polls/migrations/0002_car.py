# Generated by Django 5.1.1 on 2024-10-05 03:04

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to='')),
            ],
        ),
    ]
