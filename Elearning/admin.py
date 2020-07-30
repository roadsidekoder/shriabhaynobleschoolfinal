from django.contrib import admin
from .models import Subject, Lecture, Classroom, Homework
# Register your models here.

class HomeworkAdmin(admin.ModelAdmin):
	list_display  = ('name', 'classroom',)
	ordering = ('classroom',)
	list_filter = ('classroom', 'added')
	search_fields = ('name', 'classroom')

class LectureAdmin(admin.ModelAdmin):
	list_display  = ('topic', 'classroom','subject',)
	ordering = ('classroom',)
	list_filter = ('classroom',)
	search_fields = ('topic', 'classroom')



admin.site.register(Lecture, LectureAdmin)
admin.site.register(Subject)
admin.site.register(Classroom)
admin.site.register(Homework, HomeworkAdmin)