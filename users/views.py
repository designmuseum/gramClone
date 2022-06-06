from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import *
from gramApp.models import *
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created successfully! You can now login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def home(request):
    form = UserRegistrationForm(request.POST)
    return render(request, 'users/home.html',{"form": form})

@login_required
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    count = imgComment.objects.count()
    user = profile.user
    images = Image.objects.filter(author=user).order_by('-uploadDate')
       
     
    return render(request, 'users/profile.html', {'images': images, 'count': count})
    




'''
def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        images = Image.objects.filter(author=user).order_by('-uploadDate')
       
        context = {
            'images': images,
            'profile': profile,
            'images': images,
        }
        return render(request, 'users/profile.html')

'''






@login_required
def updateProfile(request):
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if userForm.is_valid() and profileForm.is_valid:
            userForm.save()
            profileForm.save()
            messages.success(request, f'Account updated successfully!')
            return redirect('profile')

    else:
        userForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/editProfile.html', {"userForm":userForm, "profileForm":profileForm, "profileForm":profileForm})