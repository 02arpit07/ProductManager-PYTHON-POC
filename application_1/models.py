from django.db import models

from django.contrib.auth.models import User
from django.urls import  reverse
from datetime import datetime,date

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    product_image = models.ImageField(null=True,blank=True,upload_to="images/")
    gender = models.CharField(max_length=10)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail',args=(str(self.id)))
        
    


