"""
URL configuration for django_db project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import index,create_user,create_message, delete_message, add_message, edit_message, my_messages, login, logout, search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    
    path('delete_message/<uuid:message_id>/', delete_message, name='delete_message'),
    path('add_message/', add_message, name='add_message'),
    path('edit_message/<uuid:message_id>/', edit_message, name='edit_message'),
    
    path('my_messages/', my_messages, name='my_messages'),
    path('search/', search_view, name='search'),
    
    path('login/', login, name="login"),
    path('logout/', logout, name='logout'),
    
    path('create_user/', create_user, name='create_user'),
    path('create_message/', create_message, name='create_message'),
]
