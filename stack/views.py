from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import *
from . models import *
from accounts.forms import  *
from . forms import *

# Create your views here.

def home(request):
    blogs = Blog.objects.all().order_by('-id')
    questions = Question.objects.all().order_by('-id')
    context ={
        'blogs':blogs,
        'questions':questions
    }
    return render(request, 'stack/home.html', context)

def like_blog(request, slug):
    blog = get_object_or_404(Blog, slug=request.POST.get('blog_slug'))  
    is_liked = False
    if   blog.likes.filter(id= request.user.id).exists():
        blog.likes.remove(request.user)
        is_liked = False
    else:
        blog.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(reverse('blog_details', args=[str(slug)]))


def blog_details(request, slug):
    
    blog = get_object_or_404(Blog, slug=slug)
    comments = Comment.objects.filter(blog=blog).order_by('-id')[:2]

    is_liked = False
    if  blog.likes.filter(id= request.user.id).exists():
        is_liked=True
    form = CommentsForm()
    if request.method == "POST":
        form = CommentsForm(request.POST, request.FILES)
           
            
        if form.is_valid():  
                comment = form.save(commit=False)   
                comment.author = request.user
                comment.blog = blog
                comment.save()
                return redirect('blog_details', slug=blog.slug)
    
    context = {
        'blog':blog,
        'total_likes':blog.total_likes(),
        'is_liked':is_liked,
        'form':form,
        'comments':comments,
    }
    
    return render(request, 'stack/postdetails.html', context)
    
def edit_blog(request, id):
    # blog = Blog.objects.get(id=id)
    blog = get_object_or_404(Blog, id = id)
    

    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
    context = {
        'blog':blog,
        'form':form,
    }
    return render(request, 'stack/updateblog.html', context)    
    
def postblog(request):
    if request.user.is_authenticated:
        form = BlogForm() 
        if request.method == "POST":
            form = BlogForm(request.POST, request.FILES)
           
            
            if form.is_valid():  
                blog = form.save(commit=False)   
                blog.author = request.user
                blog.save()
                return redirect('postblog')
    
        context = {
            'form':form,
        }
        return render(request, 'stack/postblogpage.html', context)

@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id = id)
    blog.delete()
    return redirect('user_page')

    
    
def userposts(request):
    blogs = Blog.objects.filter(author=request.user.id).order_by('-id')
    questions = Question.objects.filter(author=request.user.id).order_by('-id')
    context ={
        'blogs':blogs,
        'questions':questions,
    }
    return render(request, 'stack/userpage.html', context)    
    
    
def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answers = Answer.objects.filter(question=question).order_by('-id')[:2]

    accept = AcceptForm()
    form = AnswerForm()
    if request.method =='POST':
        accept = AcceptForm(request.POST)

        if form.is_valid():
            accept = form.save(commit=False)
            accept.is_helpful = question
            # answer.author = request.user
                # question
                # author
                # body
            accept.save()
            return redirect('question_details', slug=question.slug)

    
   
    if request.method =='POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question_details', slug=question.slug)

    context={
       'question':question,
        'answers':answers,
        # 'total_upvotes':answer.total_upvotes(),
        'form':form,
        'accept':accept,
    }
    return render(request, 'stack/questiondetails.html', context)

def postqn(request):
    if request.user.is_authenticated:
        form = QuestionForm() 
        if request.method == "POST":
            form = QuestionForm(request.POST, request.FILES)
           
            
            if form.is_valid():  
                question = form.save(commit=False)   
                question.author = request.user
                question.save()
                return redirect('user_page')
    
        context = {
            'form':form,
        }
        return render(request, 'stack/postqnpage.html', context)

def edit_qn(request, id):
    question = get_object_or_404(Question, id = id)
    

    form = QuestionForm(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect('user_page')
    context = {
        'question':question,
        'form':form,
    }
    return render(request, 'stack/updateqn.html', context) 

def delete_qn(request, id):
    question = get_object_or_404(Question, id = id)
    question.delete()
    return redirect('user_page')


# def vote_answer(request, slug):
#     answer = get_object_or_404(Answer, slug=request.POST.get('answer_id'))  
#     is_upvoted = False
#     if   answer.up_votes.filter(id= request.user.id).exists():
#         answer.up_votes.remove(request.user)
#         is_upvoted = False
#     else:
#         answer.up_votes.add(request.user)
#         is_upvoted = True
#     # return HttpResponseRedirect(reverse('question_details', args=[str(slug)]))    
    
    
def update_ans(request, id):
    answer = get_object_or_404(Answer, id = id)
    
    form = AnswerForm(request.POST or None, instance=answer)
    if form.is_valid():
        form.save()
        # return HttpResponseRedirect(reverse('question_details', args=[str(slug)]))
    context={
        'answer':answer,
        'form':form
    }    

    return render(request, 'stack/updateans.html', context)    

# def delete_ans(request, id):
#     answer = get_object_or_404(Answer, id = id)
#     answer.delete()
#     return redirect('question_details', slug=question.slug)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   