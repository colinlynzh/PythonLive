from django.db import models

# Create your models here.
from userApp.models import User
class Essay(models.Model):
    owner = models.ForeignKey(User,related_name="essay_owner")
    content = models.TextField()
