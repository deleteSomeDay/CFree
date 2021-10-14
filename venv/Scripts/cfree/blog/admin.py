from django.contrib import admin
from blog.models import Post
from django import forms
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Post, PostAdmin)

