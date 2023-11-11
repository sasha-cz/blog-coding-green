from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    profile = models.CharField(max_length=200)
    description = models.TextField()
    additional_body = models.TextField(blank=True)
    technology = models.CharField(max_length=20, blank=True)
    technology2 = models.CharField(max_length=20, blank=True)
    technology3 = models.CharField(max_length=20, blank=True)
    thumb = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title
        
