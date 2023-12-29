from django.db import models
from urllib.parse import urlparse

class Blogpost(models.Model):
    title = models.CharField(max_length=100) 
    slug = models.SlugField()
    body_1 = models.TextField()
    body_2 = models.TextField(blank=True)
    body_3 = models.TextField(blank=True)
    body_4 = models.TextField(blank=True)
    body_5 = models.TextField(blank=True)
    body_6 = models.TextField(blank=True)
    clickable_word = models.CharField(max_length=255, blank=True, null=True)
    hyperlink = models.URLField(blank=True, null=True)
    clickable_image_credit = models.CharField(max_length=255, blank=True, null=True)
    hyperlink_credit = models.URLField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default='Alexandra Pietroch') 
    thumb = models.ImageField(default='default.png', blank=True)
    approval_status = models.CharField(max_length=10, default='pending') 
    

    def __str__(self): 
        return self.title
    
    def snippet(self):  
        return self.body_1[:50] + '...'
    


    