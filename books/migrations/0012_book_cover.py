# Generated by Django 2.2.6 on 2020-08-09 07:09

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20200809_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=cloudinary.models.CloudinaryField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
