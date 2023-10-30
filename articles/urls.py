from django.urls import path
from . import views

app_name = 'articles' # Namespace for the app (optional)

urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('articles/submit/', views.submit_blog_post, name='submit_blog_post'),
     path('articles/submission_received', views.submission_received, name='submission_received'),
]