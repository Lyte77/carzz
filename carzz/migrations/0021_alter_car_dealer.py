# Generated by Django 5.1.3 on 2024-11-28 22:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carzz', '0020_alter_car_dealer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='dealer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='carzz.dealerprofilemodel'),
        ),
    ]