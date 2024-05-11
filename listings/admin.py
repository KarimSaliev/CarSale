from django.contrib import admin
from listings.models import Category, Car
# Register your models here.

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name','brand','type','image1','image2','image3','description', 'color', 'condition', 'user', 'price', 'number')
    readonly_fields = ('image1', 'image2', 'image3')
    fields = ('name','brand','type','image1','image2','image3','description', 'color', 'condition', 'user', 'price','number')
    search_fields = ('name',)
    ordering = ('name',)