from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
                                            PageNotAnInteger
from django.views.generic import ListView

# Create your views here.
from Nobles.models import Gallery, Faculty, Notice, Infrastructure_and_Facilities, Achievements, Download, Toppers, schoolClassroom

from Elearning.models import Classroom
def index(request):
    notices = Notice.published.all()
    infra = Infrastructure_and_Facilities.objects.all()
    achievements = Achievements.objects.all()
    # class_8_top = Toppers.objects.filter(student__classroom="Class 8")
    # class_10_top = Toppers.objects.filter(student__classroom="Class 10")
    # class_12science_top = Toppers.objects.filter(student__classroom="Class 12 (Science)")
    return render(request,'Nobles/html/index.html', { 'notices' : notices, 'infrastructures' : infra, 'achievements' : achievements})

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

# def all_notices(request):
#     notices = Notice.objects.all()
#     return render(request,'Nobles/html/all_notices.html', {'notices' : notices})

class NoticeListView(ListView):
    queryset = Notice.published.all()
    context_object_name = 'notices'
    #paginate_by = 3
    template_name = 'Nobles/html/all_notices.html'

def notice_detail(request, year, month, day, notice):
    notice = get_object_or_404(Notice, slug=notice,
                            status='published',
                            publish__year = year,
                            publish__month = month,
                            publish__day = day)

    return render(request,'Nobles/html/notice_detail.html', {'notice' : notice})

def infrastructure_facilities(request):
    infra = Infrastructure_and_Facilities.objects.all()
    return render(request, 'Nobles/html/infrastructure_facilities.html', {'infrastructures' : infra})

def admission(request):
    return render(request,'Nobles/html/admission_and_fees.html')

def download(request):
    files = Download.objects.order_by('-created_date')
    return render(request, 'Nobles/html/download.html', {'files' : files})

def homework(request):
    classes = Classroom.objects.all()
    return render(request, 'Nobles/html/homework.html', {'classes' : classes})

def toppers(request):
    classrooms = schoolClassroom.objects.all().order_by('cid')
    classroomsSessionEnd = str(classrooms[0].session_start.year + 1)[-2:] if classrooms else '2222';
    return render(request, 'Nobles/html/toppers.html', {'classrooms': classrooms, 'classroomsSessionEnd': classroomsSessionEnd})
