# Generated by Django 5.1.3 on 2024-12-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carzz', '0033_alter_car_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='car_images/'),
        ),
    ]