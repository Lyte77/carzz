# Generated by Django 5.1.3 on 2024-12-05 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carzz', '0028_car_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
