# Generated by Django 5.1.3 on 2025-01-17 14:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carzz', '0005_alter_car_thumbnail_alter_carimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealerprofilemodel',
            name='pic',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='profile-img'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='profile-img'),
            preserve_default=False,
        ),
    ]
