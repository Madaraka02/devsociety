from .models import *
from django.forms import ModelForm



class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'slug', 'content']


class CommentsForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']