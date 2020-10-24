from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils import timezone
import os
from uuid import uuid4


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='images/profile_picture/',blank=True)
    profile_picture_thumbnail = ImageSpecField(source='profile_picture',
                                      processors=[ResizeToFill(256, 256)],
                                      format='JPEG',
                                      options={'quality': 50})
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
    class Meta:
         ordering = ['first_name']
    
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='images/profile_picture/', blank=True)
    profile_picture_thumbnail = ImageSpecField(source='profile_picture',
                                      processors=[ResizeToFill(256, 256)],
                                      format='JPEG',
                                      options={'quality': 50})
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    cid = models.IntegerField(null=True)
    user = models.ManyToManyField(User, blank=True)
    subject = models.ManyToManyField("Elearning.Subject")
    cover_photo = models.ImageField(upload_to='images/', null=True, blank=True)
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
    class Meta:
         ordering = ['name']
    


class Lecture(models.Model):
    topic = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=100,
                            unique_for_date='publish')
    video_detail = models.TextField(blank=True, null=True)
    # video = models.FileField(upload_to = 'files/')
    video = models.CharField(max_length=400)
    classroom = models.ForeignKey('Elearning.Classroom', on_delete=models.CASCADE)
    subject = models.ForeignKey('Elearning.Subject', on_delete=models.CASCADE)
    homework = models.ManyToManyField('Elearning.Homework',blank=True)
    publish = models.DateField('date created', default=timezone.now)
    created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ('publish',)
    
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
    subject = models.ForeignKey('Elearning.Subject',on_delete=models.CASCADE, null=True)
    added = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
         verbose_name_plural = "Homeworks"
         ordering = ['-added']