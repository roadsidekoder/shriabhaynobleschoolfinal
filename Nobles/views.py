from django.shortcuts import render

# Create your views here.
from Nobles.models import Gallery, Faculty, Notice, Infrastructure_and_Facilities, Achievements, Download, Toppers
def index(request):
    notices = Notice.objects.all()
    infra = Infrastructure_and_Facilities.objects.all()
    achievements = Achievements.objects.all()
    class_8_top = Toppers.objects.filter(student__name="Class 8")
    class_10_top = Toppers.objects.filter(student__name="Class 10")
    class_12_top = Toppers.objects.filter(student__name="Class 12")
    return render(request,'Nobles/html/index.html', {'notices' : notices, 'infrastructures' : infra, 'achievements' : achievements,'class_8_top' : class_8_top, 'class_10_top' : class_10_top, 'class_12_top' : class_12_top})

def about(request):
    return render(request,'Nobles/html/about.html')

def bus_route_plan(request):
    return render(request,'Nobles/html/bus_route_plan.html')

def gallery(request):
	gallery = Gallery.objects.all()
	return render(request,'Nobles/html/gallery.html', {'gallery' : gallery,}) # first' : first, 'latest_album' : latest_album 

def gallery_ahead(request,num):
	gallery = Gallery.objects.get(pk=num)
	
	return render(request,'Nobles/html/gallery_ahead.html',{'gallery' : gallery })

def principal_message(request):
    return render(request,'Nobles/html/principal_message.html')

def facilities(request):
    return render(request,'Nobles/html/facilities.html')

def route_plan(request):
    return render(request,'Nobles/html/route_plan.html')

def achievements(request):
    achievements = Achievements.objects.all()
    return render(request,'Nobles/html/achievements.html', {'achievements' : achievements})

def achievement_details(request,num):
    details = Achievements.objects.get(pk=num)
    achievements = Achievements.objects.all()
    return render(request,'Nobles/html/achievement_details.html', {'details' : details, 'achievements' : achievements})

def academic_achievements(request):
    return render(request,'Nobles/html/academic_achievements.html')

def faculty(request):
    faculty = Faculty.objects.order_by('name')
    return render(request,'Nobles/html/faculty.html',{'faculty' : faculty})

def contact(request):
    return render(request,'Nobles/html/contact.html')

def all_notices(request):
    notices = Notice.objects.all()
    return render(request,'Nobles/html/all_notices.html', {'notices' : notices})

def notice_ahead(request,num):
    notices = Notice.objects.get(pk=num)
    notices_all = Notice.objects.all()
    return render(request,'Nobles/html/notice_ahead.html', {'notices' : notices, 'notices_all' : notices_all})

def infrastructure_facilities(request):
    infra = Infrastructure_and_Facilities.objects.all()
    return render(request, 'Nobles/html/infrastructure_facilities.html', {'infrastructures' : infra})

def admission(request):
    return render(request,'Nobles/html/admission_and_fees.html')

def download(request):
    files = Download.objects.all()
    return render(request, 'Nobles/html/download.html', {'files' : files})

def toppers(request):
    class_1_top = Toppers.objects.filter(student__name="Class 1")
    class_2_top = Toppers.objects.filter(student__name="Class 2")
    class_3_top = Toppers.objects.filter(student__name="Class 3")
    class_4_top = Toppers.objects.filter(student__name="Class 4")
    class_5_top = Toppers.objects.filter(student__name="Class 5")
    class_6_top = Toppers.objects.filter(student__name="Class 6")
    class_7_top = Toppers.objects.filter(student__name="Class 7")
    class_8_top = Toppers.objects.filter(student__name="Class 8")
    class_9_top = Toppers.objects.filter(student__name="Class 9")
    class_10_top = Toppers.objects.filter(student__name="Class 10")
    class_11science_top = Toppers.objects.filter(student__name="Class 11(Science)")
    class_12science_top = Toppers.objects.filter(student__name="Class 12 (Science)")
    class_11commerce_top = Toppers.objects.filter(student__name="Class 11(Commerce)")
    class_12commerce_top = Toppers.objects.filter(student__name="Class 12(Commerce)")
    class_11arts_top = Toppers.objects.filter(student__name="Class 11(Arts)")
    class_11agr_top = Toppers.objects.filter(student__name="Class 11 Agr.(Science)")
    return render(request, 'Nobles/html/toppers.html', {'class_1_top' : class_1_top,'class_2_top' : class_2_top,'class_3_top' : class_3_top,'class_4_top' : class_4_top,'class_5_top' : class_5_top,'class_6_top' : class_6_top,'class_7_top' : class_7_top,'class_8_top' : class_8_top,'class_9_top' : class_9_top, 'class_10_top' : class_10_top, 'class_11science_top' : class_11science_top,'class_12science_top' : class_12science_top,'class_11commerce_top' : class_11commerce_top,'class_12commerce_top' : class_12commerce_top,'class_11arts_top' : class_11arts_top,'class_11agr_top' : class_11agr_top,})
