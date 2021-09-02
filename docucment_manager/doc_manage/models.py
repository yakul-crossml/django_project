from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils import timezone

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    pdf = models.FileField(validators=[FileExtensionValidator(['pdf'])], upload_to='pdf_files')
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.user.username + self.title

