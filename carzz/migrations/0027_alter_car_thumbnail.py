# Generated by Django 5.1.3 on 2024-12-03 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carzz', '0026_rename_images_carimage_image_carimage_view_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='car_images/'),
        ),
    ]