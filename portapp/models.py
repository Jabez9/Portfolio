from django.db import models

# Create your models here.
class Portapp(models.Model):

    name= models.CharField(max_length=100, blank = False)

    email = models.CharField(max_length = 100)

    service = models.CharField(max_length= 50)

    message = models.TextField()
