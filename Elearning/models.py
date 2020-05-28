from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subjects(models.Model):
    subject_name = models.CharField(max_length = 50)
    

class Lectures(models.Model):
    topic = models.CharField(max_length = 100)
    video = models.FileField(upload_to = 'files/')