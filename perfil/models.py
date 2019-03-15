from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ImageUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='static/img/')
    created_at = models.DateTimeField(auto_now_add=True)