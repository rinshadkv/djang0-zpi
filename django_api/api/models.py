from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=16)
    password=models.CharField(max_length=16)
    
