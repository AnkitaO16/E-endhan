from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    mobile = models.CharField(max_length=20)
    fuel = models.CharField(max_length=30,default='DEFAULT VALUE')
    ammount = models.IntegerField()
    address = models.TextField()


class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    subject = models.TextField()
    
     

