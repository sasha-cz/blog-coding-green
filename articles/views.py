from django.shortcuts import render, redirect
from blog.models import Blogpost
from .forms import BlogpostForm

# Create your views here.
# Filter the posts to include only those that have been approved by the admin 
# (and add a field then in your model to track approval status).
def article_list(request):
    blogposts = Blogpost.objects.filter(approval_status='approved').order_by('date') 
    return render(request, 'articles.html', {'articles': blogposts})

def submit_blog_post(request):
    if request.method == 'POST':
        form = BlogpostForm(request.POST)
        if form.is_valid():
            # Create a new Blogpost instance with user's input
            new_blog_post = form.save(commit=False)  # Don't save to the database yet
            new_blog_post.approval_status = 'pending'  # Set an initial status
            new_blog_post.save()  # Save the new blog post

            # Redirect to a thank you page or a confirmation message (ToDo: create that page)
            return redirect('submission_received.html') 
    else:
        form = BlogpostForm()

    return render(request, 'submit_blog_post.html', {'form': form})

def submission_received(request):
    return render(request, 'submission_received.html')