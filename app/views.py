from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, user=request.user)  # Ensure the user owns the message
    if request.method == 'POST':
        message.delete()
        return redirect('index')  # Redirect to the home page or wherever you wish
    else:
        # If not a POST request, just redirect to home page or show an error
        return redirect('index')
    
def index(request):
    # Retrieve all message objects from the database
    messages = Message.objects.all()

    # Pass messages to the template
    context = {
        'messages': messages
    }

    return render(request, 'index.html', context)