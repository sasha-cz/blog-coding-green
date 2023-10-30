from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# Do I need here a urls. configuration? It is actually just a feature, 
# on the other hand I might need singel webpages to render each blogpost in the future...

# *The next step is to point the root URLconf at the blog.urls module. 
