from django.shortcuts import render 
from blog.models import Blogpost
# Create your views here. 
# # View should pull the blogpost-objects

def home(request): 
    what_is_green_coding = Blogpost.objects.get(slug='what-is-green-coding') 
    # The value will be the variable created in the line above. The key string can be named whatever we want: 
    return render(request, 'home.html', {'what_is_green_coding' : what_is_green_coding})  