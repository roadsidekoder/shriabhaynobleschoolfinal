from django.contrib import admin
from django.shortcuts import get_object_or_404
from .forms import AtLeastOneRequiredInlineFormSet
# Register your models here.
from Nobles.models import Gallery, Image, Faculty, Qualification, Notice, Infrastructure_and_Facilities, Achievements, Download, Toppers, Student, Homeworks


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
			

admin.site.register(Image)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Qualification)
admin.site.register(Faculty,FacultyAdmin)
admin.site.register(Notice)
admin.site.register(Infrastructure_and_Facilities)
admin.site.register(Achievements)
admin.site.register(Download)
admin.site.register(Toppers, ToppersAdmin)
admin.site.register(Student)
admin.site.register(Homeworks)