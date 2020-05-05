from django.urls import path
from django.contrib.auth import views as auth_views



from . import views


urlpatterns = [
    path('login_page/', views.login_page, name='login_page'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]