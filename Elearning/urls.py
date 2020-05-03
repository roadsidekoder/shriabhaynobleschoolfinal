from django.urls import path


from . import views

urlpatterns = [
    path('login_page/', views.login_page, name='login_page'),
    path('login/', views.user_login, name='login'),
]