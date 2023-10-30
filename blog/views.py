from django.shortcuts import render
from .models import Blogpost  

# Create your views here.
def index(request):
    blogpost =Blogpost.objects.all() # possible addition: .order_by("date") 
    return render(request, "") # find out: what does "" exactly?