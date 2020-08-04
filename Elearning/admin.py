from django.contrib import admin
from .models import Subject, Lecture, Classroom, Homework, Student
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

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','user', )


admin.site.register(Lecture, LectureAdmin)
admin.site.register(Subject)
admin.site.register(Classroom)
admin.site.register(Student,StudentAdmin)
admin.site.register(Homework, HomeworkAdmin)