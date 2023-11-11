from django.urls import path, re_path
from . import views

app_name = 'home'
urlpatterns = [
    path('home/', views.home, name='homepage'),
    # Define slug as named capturing group
    re_path(r'^home/(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
]
