from.views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('addblog/', postblog, name="postblog"),
    path('user/', userposts, name="user_page"),
    path('like/<slug:slug>/', like_blog, name="like_blog"),

        # BLOG URLS
    path('blogs/<slug:slug>/', blog_details, name="blog_details"),
    path('blog/edit/<int:id>/', edit_blog, name="edit_blog"),
    path('blog/delete/<int:id>/', delete_blog, name="delete_blog"),

    # QUESTION URLS
    path('questions/<slug:slug>/', question_details, name="question_details"),
    path('postqn/', postqn, name="postqn"),
    path('questions/delete/<int:id>/', delete_qn, name="delete_qn"),
    path('questions/edit/<int:id>/', edit_qn, name="edit_qn"),


    path('ans/edit/<int:id>/', update_ans, name="update_ans"),

#    AUTHENTICATION URLS
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
