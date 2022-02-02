from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.user_register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('postblog', views.post_blog, name='postblog'),
    path('blog_detail/<int:id>', views.blog_detail, name='blog_detail'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),


]