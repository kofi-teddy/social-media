# Generated by Django 3.0.6 on 2020-05-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
