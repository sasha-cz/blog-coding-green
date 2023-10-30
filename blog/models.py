from django.db import models

#  requirements: pull all the posts and enable creating a new post
#  what fields should the model have, and how will the schema look like.

# Create your models here.
class Blogpost(models.Model):
    # define different fields - what is going to be stored in a blogpost
    title = models.CharField(max_length=100) # what type of data will be received
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approval_status = models.CharField(max_length=10, default='pending')
    # add in author later --> A foreign key to a user model or an author's profile, representing the author of the blog post
    # add in Featured Image later --> image associated with the blog post
    # add in Likes and Comments later
    # add in Views later
    # add in Category later --> A foreign key or a many-to-many relationship to a category model. This helps categorize and organize blog posts
    # add in Tags later --> keywords or labels that describe the content of the post

# To pull all objects(instances) with readable titles unlike "object no 1,2,3...", use the following function:
    def __str__(self): # self = instance of the article
        return self.title
    
    # additional front end improvement to not show the whole body per blogpost
    def snippet(self):  # model method :  self = instance of the article
        return self.body[:50] + '...'
    