from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def chat_index(request):
    context = {'title': 'Chat'}
    return render(request, 'chat/index.html', context)
@login_required
def room(request, room_name):
    context = {'title': 'Room', 'room_name':room_name}
    return render(request, 'chat/room.html', context)

