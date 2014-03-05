from django.shortcuts import render
from messages.models import Message

# Create your views here.

def home(request):
    if 'text' in request.GET:
        author_ = request.GET['author']
        text_ = request.GET['text']

        message = Message(author=author_, text=text_)
        message.save()

    messages = Message.objects.all()

    return render(request, 'home.html', {'messages': messages})
