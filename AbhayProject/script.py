from django.contrib.auth.models import User
def users():
    
    user=User.objects.create_user('foo', password='bar')
    user.is_staff=True
    user.save()