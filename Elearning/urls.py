from django.urls import path
from django.contrib.auth import views as auth_views



from . import views


urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('classroom/', views.classroom, name='classroom'),
    # #path('login_page/', views.login_page, name='login_page'),
    # #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/<int:num>/<int:video_url>/', views.dashboard, name='video_pk'),   #https://stackoverflow.com/questions/52456891/how-to-avoid-error-in-multiple-primary-key-path-django
]