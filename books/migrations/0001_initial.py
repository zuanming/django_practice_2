# Generated by Django 2.2.6 on 2020-08-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
        ),
    ]
