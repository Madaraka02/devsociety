from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=300, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()
    slug = models.SlugField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question =  models.ForeignKey(Question, on_delete=models.CASCADE,  null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = RichTextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    is_answer_helpful = models.BooleanField(default=False, null=True, blank=True)
    # up_votes = models.ManyToManyField(User, related_name="upvotes", blank=True)

    def __str__(self):
        return self.question.title
