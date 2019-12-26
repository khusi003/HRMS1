from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length = 20)
    email = models.EmailField(unique= True)
    mobile = models.CharField(max_length = 10)
    otp = models.IntegerField(default = 459)

    