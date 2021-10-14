from django.urls import path
from .views import blogs, post_detail


app_name = 'blog'
urlpatterns = [
    path('', blogs, name='home'),
    path('post/<slug>', post_detail, name='post'),
]
