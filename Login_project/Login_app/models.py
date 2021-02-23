from django.db import models

# Create your models here.
class NewUser(models.Model):
    Username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    pwd=models.CharField(max_length=10)
    Gender=models.CharField(max_length=1)

