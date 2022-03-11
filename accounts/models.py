from xml.sax.handler import property_declaration_handler
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=300, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(null=True)
    slug = models.SlugField(null=True)
    content = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    def __str__(self):
        return self.title
        
  
    def total_likes(self):
        return self.likes.count() 

class Comment(models.Model):
    blog =  models.ForeignKey(Blog, on_delete=models.CASCADE,  null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = RichTextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.blog.title

