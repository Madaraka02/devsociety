from.views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('addblog/', postblog, name="postblog"),
    path('like/<slug:slug>/', like_blog, name="like_blog"),
    path('blogs/<slug:slug>/', blog_details, name="blog_details"),
    path('blog/edit/<int:id>/', edit_blog, name="edit_blog"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
