# Generated by Django 5.1.3 on 2024-11-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carzz', '0015_carimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='carimage',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]