from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from user.forms import UserLoginForm, UserRegistrationForm, BioChangeForm, UserProfileForm
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from user.models import UserBio
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST) # data from request variable
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('listings:index'))

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'user/login.html',context)
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('listings:index'))

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! You've successfully registered")
            return HttpResponseRedirect('login')
    else:

        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'user/register.html',context)


def profile(request, change_id=None):
    if request.method == 'POST' and change_id == 'account-general':
        form_general = UserProfileForm(instance = request.user, data = request.POST)
        if form_general.is_valid():
            form_general.save()
            messages.success(request, "Info Changed")
            return HttpResponseRedirect(reverse('listings:index'))
        else:
            print(form_general.errors)
    else:
        form_general = UserProfileForm(instance = request.user)
    if request.method == 'POST' and change_id == 'account-change-password':
        form_password = PasswordChangeForm(request.user, data=request.POST)
        if form_password.is_valid():
            form_password.save()
            update_session_auth_hash(request, form_password.user)
            messages.success(request, "Password Changed")
            return HttpResponseRedirect(reverse('listings:index'))
    else:
        form_password = PasswordChangeForm(request.user)
    if request.method == 'POST' and change_id == 'account-info':
        form_bio = BioChangeForm(data=request.POST)
        if form_bio.is_valid():
            bio = form_bio.cleaned_data['bio']
            birthday = form_bio.cleaned_data['birthday']
            country = form_bio.cleaned_data['country']
            number = form_bio.cleaned_data['number']
            user = request.user
            bio_model = UserBio(bio=bio, birthday=birthday, country=country, number=number, user=user)
            bio_model.save()
            return HttpResponseRedirect(reverse('listings:index'))
    else:
        try:
            current_bio = UserBio.objects.get(user=request.user)
            initial = {'bio': current_bio.bio, 'birthday':current_bio.birthday, 'country':current_bio.country, 'number':current_bio.number}
            form_bio = BioChangeForm(initial=initial)
        except UserBio.DoesNotExist:
            form_bio = BioChangeForm()

    context = {'title': 'Profile', 'form_general': form_general, 'form_password':form_password, 'form_bio':form_bio}
    return render(request, 'user/profile.html', context)

def external_user(request, user_id=None):
    user = User.objects.get(id=user_id)
    request.session['user'] = {'user_id':user_id}
    bio = UserBio.objects.get(user=user)
    context = {'title': 'User Profile', 'bio':bio, 'user':user}
    return render(request, 'user/external_profile.html', context)