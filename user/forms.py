
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.http import request

from user.models import UserBio
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your password'
    }))
    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control ', 'placeholder': 'Enter your last name'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your username'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm password'
    }))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class BioChangeForm(forms.Form):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':
                                                       'form-control'}), required=False)
    birthday = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}
        )
    )
    country = forms.CharField(widget=forms.TextInput(attrs={'class':
                                                       'form-control'}), required=False)
    number = forms.CharField(widget=forms.TextInput(attrs={'class':
                                                       'form-control'}), required=False)

    class Meta:
        model = UserBio
        fields = ('bio', 'date', 'country', 'number')