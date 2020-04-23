from django.urls import path


from . import views

urlpatterns = [
        path('', views.index, name='home'),
        path('about/', views.about, name='about'),
        path('bus_route_plan/', views.bus_route_plan, name='bus_route_plan'),
        path('gallery/', views.gallery, name='gallery'),
        path('gallery/<int:num>/', views.gallery_ahead, name='gallery_pk'),
        path('principal_message/', views.principal_message, name='message'),
        path('facilities/', views.facilities, name='facilities'),
        path('route_plan/', views.route_plan, name='route_plan'),
        path('achievements/', views.achievements, name='achievements'),
        path('achievements/<int:num>/', views.achievement_details, name='achievement_pk'),
        path('notice/', views.all_notices, name='all_notices'),
        path('notice/<int:num>/', views.notice_ahead, name='notice_pk'),
        path('academic_achievements/', views.academic_achievements, name='academic_achievements'),
        path('faculty/', views.faculty, name='faculty'),
        path('contact/', views.contact, name='contact'),
        path('infrastructure_facilities/', views.infrastructure_facilities, name='infrastructure_facilities'),
        path('admission/', views.admission, name='admission'),
        path('download/', views.download, name='download'),
        path('toppers/', views.toppers, name='toppers'),
        path('homework/', views.homework, name='homework'),
]