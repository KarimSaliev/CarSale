from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Car(models.Model):
    name = models.CharField(null=False, max_length=128)
    brand = models.CharField(null=True, max_length=128)
    type = models.ForeignKey(null=True, to=Category, on_delete=models.CASCADE)
    image1 = models.ImageField(null=True,upload_to='cars_images')
    image2 = models.ImageField(null=True,upload_to='cars_images')
    image3 = models.ImageField(null=True,upload_to='cars_images')
    description = models.TextField(null=True, blank=True)
    color = models.CharField(null=True, max_length=128)
    condition = models.CharField(null=True, max_length=128)
    user = models.ForeignKey(null=False, to=User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number = models.CharField(null=True, max_length=20)

