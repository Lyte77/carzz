# Generated by Django 5.1.3 on 2024-12-03 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carzz', '0025_rename_image_car_thumbnail_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carimage',
            old_name='images',
            new_name='image',
        ),
        migrations.AddField(
            model_name='carimage',
            name='view_type',
            field=models.CharField(choices=[('front', 'Front View'), ('rear', 'Rear View'), ('back', 'Back View'), ('interior', 'Interior View'), ('other', 'Other View')], default='other', max_length=50),
        ),
    ]