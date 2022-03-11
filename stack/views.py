from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from accounts.models import *
from . models import *
from accounts.forms import  *

# Create your views here.

def home(request):
    blogs = Blog.objects.all().order_by('-id')
    context ={
        'blogs':blogs
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

    is_liked = False
    if  blog.likes.filter(id= request.user.id).exists():
        is_liked=True

    
    context = {
        'blog':blog,
        'total_likes':blog.total_likes(),
        'is_liked':is_liked
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
    
        context = {
            'form':form,
        }
        return render(request, 'stack/userpage.html', context)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   