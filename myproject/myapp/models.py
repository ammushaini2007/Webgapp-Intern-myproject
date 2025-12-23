from django.db import models

# Create your models here.
class Forms(models.Model):
    name=models.CharField(max_length=100,null=True)
    number=models.IntegerField(default=0)
    dob=models.DateField(null=True, blank=True) 
    father=models.CharField(max_length=100,null=True)
    mobile=models.IntegerField(default=0)
    email=models.EmailField(max_length=200,null=True)
    password=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    department=models.CharField(max_length=100,null=True)
    Gender=models.CharField(max_length=100,null=True)




    