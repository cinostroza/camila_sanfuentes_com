# Generated by Django 3.2.5 on 2021-10-19 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_gallery_thumbnail_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='thumbnail_size',
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='thumbnail_size',
            field=models.CharField(choices=[('L', 'Large'), ('M', 'Medium'), ('S', 'Small')], default='S', max_length=1),
        ),
    ]
