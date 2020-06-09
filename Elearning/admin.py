from django.contrib import admin
from .models import Lectures,Subjects
# Register your models here.

class LectureAdmin(admin.ModelAdmin):
	list_display  = ('topic', 'classroom','subject',)
	ordering = ('classroom',)
	list_filter = ('classroom',)
	search_fields = ('topic', 'classroom')


admin.site.register(Lectures, LectureAdmin)
# admin.site.register(Section)
admin.site.register(Subjects)