# Generated by Django 2.2.6 on 2020-08-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_author_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cost',
            field=models.DecimalField(decimal_places=3, default=10, max_digits=10),
            preserve_default=False,
        ),
    ]
