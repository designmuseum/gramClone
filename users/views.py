from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import  CreateView
from .email import send_welcome_email

from .forms import *
from gramApp.models import *
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            form.save()
            # send_welcome_email(username,email)
            HttpResponseRedirect('login')
            # return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def home(request):
    form = UserRegistrationForm(request.POST)
    return render(request, 'users/home.html',{"form": form})


class ProfileView(LoginRequiredMixin,View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        


        user = profile.user
        count = imgComment.objects.count()
        images = Image.objects.filter(author=user).order_by('-uploadDate')
        # comments = imgComment.filter(Image_id = id)

        followers = profile.followers.all()
        if len(followers) == 0:
            isFollowing = False

        for follower in followers:
            if follower == request.user:
                isFollowing = True
                break
            else:
                isFollowing = False


        following = profile.following.all()

      
        getFollowers = len(followers)
        getFollowing=len(following)

        context = {
            'user': user,
            'profile': profile,
            'images': images,
            'count': count,
            'getFollowers': getFollowers,
            'isFollowing': isFollowing,
            'getFollowing': getFollowing,
            
        }

        return render(request, 'users/profile.html', context)

class follow(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.add(request.user)
        profile.following.add(request.user)

        return redirect('profile', pk=profile.pk)

class unFollow(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.remove(request.user)
        profile.following.remove(request.user)

        return redirect('profile', pk=profile.pk)

@login_required
def updateProfile(request,pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request, f'Account updated successfully!')
            return redirect('profile',pk)

    else:
        userForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/editProfile.html', {"userForm":userForm, "profileForm":profileForm, "profileForm":profileForm})


@login_required
def profileSearch(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'users/search.html', params)
    else:
        message = "Search couldn't be completed..."
    return render(request, 'users/search.html', {'message': message})