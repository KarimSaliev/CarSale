from django.urls import path
from user.views import login, register, logout, profile, external_user

app_name = 'user'
urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('profile', profile, name='profile'),
    path('profile/<str:change_id>/', profile, name='profile'),
    path('ex_profile/<int:user_id>/', external_user, name='external_user')
]