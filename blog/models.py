from django.db import models


class Blogpost(models.Model):
    title = models.CharField(max_length=100) 
    slug = models.SlugField()
    body_1 = models.TextField()
    body_2 = models.TextField(blank=True)
    body_3 = models.TextField(blank=True)
    body_4 = models.TextField(blank=True)
    body_5 = models.TextField(blank=True)
    body_6 = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default='Alexandra Pietroch') 
    thumb = models.ImageField(default='default.png', blank=True)
    approval_status = models.CharField(max_length=10, default='pending')
    # add Comments later
    # add in Views later
    # add in Category later --> A foreign key or a many-to-many relationship to a category model.
    # add in Tags later --> keywords or labels that describe the content of the post

    def __str__(self): 
        return self.title
    
    def snippet(self):  # model method :  self = instance of the article
        return self.body_1[:50] + '...'
    