# Generated by Django 5.0.2 on 2024-03-03 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_userbio_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbio',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='userbio',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
