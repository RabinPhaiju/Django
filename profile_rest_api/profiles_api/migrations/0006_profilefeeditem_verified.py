# Generated by Django 3.2.7 on 2022-02-07 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0005_profilefeeditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilefeeditem',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]