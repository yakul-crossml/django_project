from django.db import models
import datetime
now=datetime.datetime.now()
# Create your models here.
class Expense(models.Model):
    travel=models.IntegerField(default=0)
    eduction=models.IntegerField(default=0)
    gifts=models.IntegerField(default=0)
    Investments=models.IntegerField(default=0)
    Bills=models.IntegerField(default=0)
    Food=models.IntegerField(default=0)
    Health=models.IntegerField(default=0)
    Personal=models.IntegerField(default=0)
    fee=models.IntegerField(default=0)
    time= models.DateTimeField(default=now)
class Budget(models.Model):
    bgt=models.IntegerField(default=0)