from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lectures
from Nobles.models import Student

from .forms import LoginForm

# Create your views here.

@login_required
def dashboard(request,num, video_url):
    sections = Student.objects.get(pk=num)   # class 1
    list = []
    lecture_list = []
    
    for sec in sections.subject.all():
        list.append(int(sec.id))                   



    for sub_id in list:
        lecture_list.append(Lectures.objects.filter(classroom__id=num, subject__id=sub_id))
    #     lecture_dic[sub_id] = Lectures.objects.filter(classroom__id=num, subject__id=sub_id)

        # lecture_list.append(Lectures.objects.filter(classroom__id=num, subject__id=sub_id))
    
    # section = Section.objects.filter(classroom__id = num)[0]
    lecture_url = Lectures.objects.get(pk=video_url)
    return render(request, 'Elearning/dashboard.html', {'lecture_list' : lecture_list, 'sections' : sections, 'lecture_url': lecture_url})

@login_required
def classroom(request):
    sections = Student.objects.all()
    return render(request, 'Elearning/classroom.html', { 'sections' : sections})

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

