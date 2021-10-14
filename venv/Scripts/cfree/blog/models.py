from django.db import models
import datetime
from tinymce import models as tinymce_models
# Create your models here.


class Post(models.Model):

    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()
    image = models.ImageField(upload_to='img')
    altimg = models.CharField(max_length=100)

    class Meta:
          ordering = ['-timestamp',]
