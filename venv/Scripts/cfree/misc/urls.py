from django.urls import path
from .views  import  mission
from .views  import  about
from .views import signup


app_name = 'misc'
urlpatterns = [
    path('mission', mission, name='mission'),
    path('about', about, name='about'),
    path('signup', signup, name='signup')
]