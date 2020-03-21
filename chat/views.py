from django.shortcuts import render
# from django.template.context_processors import request
from chat.models import Room


# Create your views here.
def chat_room(request, label):
    # created returns back true if a new room was created and false if not
    room, created = Room.objects.get_or_create(label=label)
    messages = room.messages.order_by('timestamp')
    return render(request, "chat/room.html", {
        'room': room,
        'messages': messages
        })

def home(request):
    return render(request, 'chat/home.html')