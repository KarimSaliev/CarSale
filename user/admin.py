from django.contrib import admin
from user.models import UserBio
# Register your models here.
@admin.register(UserBio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('bio','birthday','country','number')
    fields = ('bio','birthday','country','number')
    search_fields = ('bio',)
    ordering = ('bio',)