from django.shortcuts import render
from blog.models import Blogpost


def home(request):  
    articles = Blogpost.objects.filter(approval_status='approved').order_by('date')
    # The value will be the variable created in the line above. The key string can be named whatever we want: 
    return render(request, 'home/main.html', {'articles': articles})  


def article_detail(request, slug):
    article = Blogpost.objects.get(slug=slug)
    return render(request, 'home/article_detail.html', {'article': article})

