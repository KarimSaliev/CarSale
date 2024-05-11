from django.contrib import admin
from chat.models import Message
from django.contrib import admin

# Register your models here.
@admin.register(Message)

class MessageAdmin(admin.ModelAdmin):
    list_display = (
    'sender', 'content', 'thread_name',)
    readonly_fields = (
    'sender', 'content', 'thread_name',)