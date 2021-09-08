from django.contrib import admin
from .models import Subject, Lecture, Classroom, Homework, Student, Teacher
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Register your models here.

class HomeworkAdmin(admin.ModelAdmin):
	list_display  = ('name', 'classroom',)
	ordering = ('classroom',)
	list_filter = ('classroom', ('added', DateRangeFilter))
	search_fields = ('name', 'classroom')

class LectureAdmin(admin.ModelAdmin):
        list_display  = ('topic', 'slug', 'publish', 'classroom','subject',)
        ordering = ('classroom',)
        list_filter = ('classroom',)
        search_fields = ('topic', 'classroom',)
        date_hierarchy = ('publish')
        prepopulated_fields = {'slug' : ('topic',)}

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','user', )
    ordering = ('first_name',)
    search_fields = ('first_name', 'user__username',)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','user', )


admin.site.register(Lecture, LectureAdmin)
admin.site.register(Subject)
admin.site.register(Classroom)
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Homework, HomeworkAdmin)