from django import forms
from blog.models import Blogpost


class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'body'] # exclude fields that should not be directly editable by users 
                                   # (e.g. the approval status field).

