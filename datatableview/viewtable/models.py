from django.db import models
from django.contrib.auth.models import Group

# Create your models here.



class Employee(models.Model):
    

    dob = models.DateField(verbose_name= 'Birtsdfsdfsfdhday',null=True, blank=True)
    phone_number = models.IntegerField(null=True , blank=True ) 
    joining_date=models.DateTimeField(verbose_name='Joining Date',null=True, blank=True)
    address=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.address