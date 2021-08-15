from django.contrib import admin
from django.shortcuts import get_object_or_404
from .forms import AtLeastOneRequiredInlineFormSet
# Register your models here.
from Nobles.models import Gallery, Image, Faculty, Qualification, Notice, Infrastructure_and_Facilities, Achievements, Download, Toppers, schoolClassroom


class ImageTabularInline(admin.TabularInline):
	model = Image
	formset = AtLeastOneRequiredInlineFormSet

class GalleryAdmin(admin.ModelAdmin):
	inlines = [ImageTabularInline,]
	class Meta:
		model = Gallery

class FacultyAdmin(admin.ModelAdmin):
    pass

class ToppersAdmin(admin.ModelAdmin):
	list_display  = ('name',)
	#def instead_marks():
	#	check = Toppers.objects.all()


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    #list_filter = ('status', 'author', 'created', 'publish')
    search_fields = ('title',)
    date_hierarchy = ('publish')
    #raw_id_fields = ('author',)
    ordering = ('status', 'publish')
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Image)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Qualification)
admin.site.register(Faculty,FacultyAdmin)
admin.site.register(Notice,NoticeAdmin)
admin.site.register(Infrastructure_and_Facilities)
admin.site.register(Achievements)
admin.site.register(Download)
admin.site.register(Toppers, ToppersAdmin)
admin.site.register(schoolClassroom)
