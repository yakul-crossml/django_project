from django.db import models

# Create your models here.
class table(models.Model):
    name=models.CharField(max_length=100)
    Document_name=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    link=models.URLField(max_length=200) 
    
    def __str__(self):
        return self.name
