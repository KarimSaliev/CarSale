from django.urls import path
from listings.views import index, publish, my_listings, listings,\
    search_car, more_details, u_listings

app_name = 'listings'
urlpatterns = [
    path('', index, name='index'),
    path('sell', publish, name='publish'),
    path('my_listings', my_listings, name='my_listings'),
    path('page/<int:page_number>/', my_listings, name='paginator'),
    path('listings', listings, name='listings'),
    path('listings_page/<int:page_number>/', listings, name='paginator2'),
    path('search_car', search_car, name='search_car'),
    path('car/<int:car_id>/', more_details, name='car'),
    path('u_listing', u_listings, name='u_listings'),
    path('u_listings_page/<int:page_number>/', u_listings, name='paginator3')
]