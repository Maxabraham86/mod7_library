from django.db import models

# Create your models here.
class Client (models.Model):
    first_name= models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email=models.EmailField(unique=True)
    height = models.DecimalField(decimal_places=2, max_digits=3)
    active = models.BooleanField(default=True) 
    #marcas temporales
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)