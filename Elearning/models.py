from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils import timezone
import os
from uuid import uuid4
#from Nobles.models import Homework
# Create your models here.


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    cid = models.IntegerField(null=True)
    user = models.ManyToManyField(User)
    subject = models.ManyToManyField("Elearning.Subject")
    cover_photo = models.ImageField(upload_to='images/', null=True)
    cover_photo_thumbnail = ImageSpecField(source='cover_photo',
                                      processors=[ResizeToFill(1280, 720)],
                                      format='JPEG',
                                      options={'quality': 50})

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['cid']
        verbose_name_plural = "Classroom"

class Subject(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    


class Lecture(models.Model):
    topic = models.CharField(max_length = 100)
    video_detail = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to = 'files/')
    classroom = models.ForeignKey('Elearning.Classroom', on_delete=models.CASCADE)
    subject = models.ForeignKey('Elearning.Subject', on_delete=models.CASCADE)
    homework = models.ManyToManyField('Elearning.Homework',blank=True)

    def __str__(self):
        return self.topic
    
class Homework(models.Model):    
    # Source : https://www.dangtrinh.com/2015/11/django-imagefield-rename-file-on-upload.html
    def path_and_rename(instance, filename):
        upload_to = 'files/'
        ext = filename.split('.')[-1]
        # get filename
        print(instance.name)
        if instance.name:
            filename = '{}_{}.{}'.format(instance.name,instance.added, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    name = models.CharField(max_length=200)
    your_file = models.FileField(upload_to=path_and_rename)
    description = models.TextField(blank=True, null=True)
    classroom = models.ForeignKey('Elearning.Classroom',on_delete=models.CASCADE)
    subject = models.ForeignKey('Elearning.Subject',on_delete=models.CASCADE)
    added = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
         verbose_name_plural = "Homeworks"
         ordering = ['added']
