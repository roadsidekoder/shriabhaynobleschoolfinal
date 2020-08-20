from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from Elearning.models import Lecture, Classroom, Homework, Student

@login_required
def teacher_portal(request):
    user_name = User.objects.get(username=request.user.username)


@login_required
def portal(request):
    user_name = User.objects.get(username=request.user.username)
    print(user_name)
    if Student.objects.filter(user__username=user_name).exists():
        try:
            classroom = Classroom.objects.get(user=user_name)
            list = []
            homework_list = []
        
            for subject in classroom.subject.all():
                list.append(int(subject.id))                   

            for sub_id in list:
                homework_list.append(Homework.objects.filter(classroom=classroom, subject__id=sub_id))
                            
        except Classroom.DoesNotExist:
            classroom = None
            homework_list = []

        lecture = Lecture.objects.filter(classroom=classroom)
        if lecture.exists():
            lecture = lecture[0].id
        else:
            lecture = None
       
        return render(request, 'Elearning/portal.html', {'classroom' : classroom, 'lecture_id' : lecture, 'homework_list': homework_list, 'user_name': user_name})
    else:
        classrooms = Classroom.objects.all()
        # homework_list = Homework.objects.all()
        lecture_id = Lecture.objects.filter(classroom=classrooms[0])
        return render(request,'Elearning/teacher-portal.html', {'classrooms' : classrooms, 'user_name': user_name, 'lecture_id': lecture_id})


@login_required
def dashboard(request, num, video_url):
    sections = Classroom.objects.get(pk=num)   # class 1
    list = []
    lecture_list = []
    
    for section in sections.subject.all():
        list.append(int(section.id))                   

    for sub_id in list:
        lecture_list.append(Lecture.objects.filter(classroom__id=num, subject__id=sub_id))

    lecture_url = Lecture.objects.get(pk=video_url)
    return render(request, 'Elearning/dashboard.html', {'lecture_list' : lecture_list, 'sections' : sections, 'lecture_url': lecture_url})

# @login_required
# def classroom(request):
#     sections = Classroom.objects.all()
#     return render(request, 'Elearning/classroom.html', { 'sections' : sections})

# def login_paged(request):
#     return render(request, 'Elearning/registration/login.html')

# def login_page(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                              username=cd['username'],
#                              password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated '\
#                                         'successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'Elearning/registration/login.html', {'form': form})

