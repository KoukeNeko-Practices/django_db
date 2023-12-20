from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Message

def create_user(request):
    # Example of creating a user
    user = User.objects.create_user('john_doe', 'john@example.com', 'johnpassword')
    user.save()
    return HttpResponse("User created successfully")

def create_message(request):
    user = User.objects.first()  # Get the first user
    if user:
        message = Message(user=user, text='Hello, world!')
        message.save()
        return HttpResponse("Message created successfully")
    else:
        return HttpResponse("No users available to attach a message")

def index(request):
    return render(request, 'index.html')