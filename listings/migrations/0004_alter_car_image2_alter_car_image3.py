# Generated by Django 5.0.2 on 2024-02-26 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_remove_car_image_car_image1_car_image2_car_image3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='cars_images'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='cars_images'),
        ),
    ]
