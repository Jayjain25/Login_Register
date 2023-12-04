from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20,null=False)
    name = models.CharField(max_length=50,null=False)
    email = models.EmailField(null=False)
    passward = models.CharField(max_length=50,null=False)
    number = models.CharField(max_length=50,null=False)