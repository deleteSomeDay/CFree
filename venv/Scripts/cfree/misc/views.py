from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def mission(req):
    return render_to_response('misc/Mission.html')

def spotlightcharity(req):
    return render_to_response('misc/SpotlightCharity.html')

def about(req):
    return render_to_response('misc/about.html')

def signup(req):
    return render_to_response('misc/signup.html')