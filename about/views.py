from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):
    about = About.objects.get(title="Nice to meet you! I'm Alexandra Pietroch")
    return render(request, 'about/main.html', {'about': about})