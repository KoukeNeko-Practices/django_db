from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
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
    
def logout(request):
    auth_logout(request)
    return redirect('/')
    
@login_required
def add_message(request):
    if request.method == 'POST':
        message_text = request.POST.get('message_text')
        if message_text:
            Message.objects.create(user=request.user, text=message_text)
        return redirect('/')  # Redirect to the index page or a confirmation page
    return redirect('/')  # Handle non-POST requests

@login_required
def edit_message(request, message_id):
    if request.user.is_superuser:
        message = get_object_or_404(Message, id=message_id)
    else:
        message = get_object_or_404(Message, id=message_id, user=request.user)
    if request.method == 'POST':
        message.text = request.POST.get('edited_message', '')
        message.save()
        return redirect('/')
    return redirect('/')

@login_required
def delete_message(request, message_id):
    if request.user.is_superuser:
        message = get_object_or_404(Message, id=message_id)
    else:
        message = get_object_or_404(Message, id=message_id, user=request.user)
    if request.method == 'POST':
        message.delete()
        return redirect('/')
    else:
        return HttpResponse("Message delete fail")

@login_required
def my_messages(request):
    user_messages = Message.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'index.html', {'messages': user_messages})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')  # Redirect to the index page after successful login
        else:
            return render(request, 'login_wrong.html')  # Render the login_wrong.html if login fails
    return render(request, 'login.html')

def index(request):
    # Retrieve all message objects from the database
    messages = Message.objects.all().order_by('-created_at')

    # Pass messages to the template
    context = {
        'messages': messages
    }
    
    return render(request, 'index.html', context)