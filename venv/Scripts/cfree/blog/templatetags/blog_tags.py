from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag()
def render_bloglist():
    entries = Post.objects.all()[:6]
    return entries

@register.simple_tag()
def render_topblog():
    entry = Post.objects.all()[:1].get()
    return entry
