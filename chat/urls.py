from django.urls import path
from chat.views import chat_index, room
app_name = 'chat'
urlpatterns = [
    path('', chat_index, name='index'),
    path('<str:room_name>/', room, name='room'),
]