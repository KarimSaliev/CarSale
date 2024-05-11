from django.shortcuts import render
from listings.forms import CarForm, CarSearch
from listings.models import Car,Category
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    featured_cars = Car.objects.all()[:3]
    latest_three_objects = Car.objects.all().order_by('-id')[:3]
    context = {'Title': 'Index', 'cars': featured_cars, 'new_cars':latest_three_objects}
    return render(request, 'listings/index.html', context)
def publish(request):
    if request.method=='POST':
        form = CarForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            brand = form.cleaned_data['brand']
            type_id = form.cleaned_data['type']
            type = Category.objects.get(pk=type_id)
            image1 = form.cleaned_data['image1']
            image2 = form.cleaned_data['image2']
            image3 = form.cleaned_data['image3']
            description = form.cleaned_data['description']
            color = form.cleaned_data['color']
            condition = form.cleaned_data['condition']
            user = request.user
            price = form.cleaned_data['price']
            car = Car(name=name, brand=brand, type=type, image1=image1, image2=image2, image3=image3, description=description,
                      color=color, condition=condition,user=user,price=price)

            car.save()


    else:
        form = CarForm()
    context = {'Title': 'Sell', 'form':form}
    return render(request, 'listings/publish.html', context)

def my_listings(request, page_number=1):
    listings = Car.objects.filter(user=request.user)
    per_page = 3
    paginator = Paginator(listings, per_page)
    listings_paginator = paginator.page(page_number)
    mine = True
    context = {'Title': 'My Listings', 'listings':listings_paginator, 'mine':mine}
    return render(request, 'listings/listings.html', context)

def listings(request, page_number=1):
    listings = Car.objects.all()
    per_page = 3
    paginator = Paginator(listings, per_page)
    listings_paginator = paginator.page(page_number)
    context = {'Title': 'Listings', 'listings': listings_paginator}
    return render(request, 'listings/listings.html', context)

def search_car(request):
    if request.method=='POST':
        form = CarSearch(data=request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            type_id = form.cleaned_data['type']
            type = Category.objects.get(pk=type_id)
            price = form.cleaned_data['price']
            color = form.cleaned_data['color']

            output = Car.objects.filter(brand__icontains=brand, type=type,price__lt=price, color__icontains = color)
            context = {'title': 'Search', 'listings': output}
            return render(request, 'listings/listings.html', context)
    else:
        form = CarSearch()
    context = {'title': 'Search', 'form':form}
    return render(request, 'listings/filter.html', context)

def more_details(request, car_id):
    car = Car.objects.get(pk=car_id)
    context = {'title': 'Car', 'car':car}
    return render(request, 'listings/listing_more.html', context)

def u_listings(request, page_number=1):
    id = request.session['user']['user_id']
    user = User.objects.get(pk=id)
    listings = Car.objects.filter(user=user)
    per_page = 3
    paginator = Paginator(listings, per_page)
    listings_paginator = paginator.page(page_number)
    userlisting = True
    context = {'Title': 'User Listings', 'listings': listings_paginator, 'userlisting': userlisting}
    return render(request, 'listings/listings.html', context)