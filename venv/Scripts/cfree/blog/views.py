from urllib.parse import quote_plus
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post

# Create your views here.


def blogs(req):
    entries = Post.objects.all()[:10]
    return render_to_response('blogs/blog_main.html', {'posts': entries})


def post_detail(req, slug):
    postd = get_object_or_404(Post, slug=slug)
    shared_quote = quote_plus(postd.bodytext)
    context = {
        'post': postd,
        'shared_string': shared_quote,
    }
    return render_to_response('blogs/post_detail.html', context)
