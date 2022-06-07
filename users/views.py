from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import DeleteView, ListView, UpdateView,DetailView, CreateView


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
def profile(self, request, pk):
    profile = Profile.objects.get(pk=pk)
    count = imgComment.objects.count()
    user = profile.user
    images = Image.objects.filter(author=user).order_by('-uploadDate')
       
     
    return render(request, 'users/profile.html', {'images': images, 'count': count})
    
class ProfileView(LoginRequiredMixin,View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        count = imgComment.objects.count()
        images = Image.objects.filter(author=user).order_by('-uploadDate')

        context = {
            'user': user,
            'profile': profile,
            'images': images,
            'count': count
        }

        return render(request, 'users/profile.html', context)

# class ImageUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView,):
#     model = Profile
#     fields=['caption']
#     template_name = 'app/updateImage.html'    
#     # success_url = '/feed/'
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)



@login_required
def updateProfile(request,pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if userForm.is_valid() and profileForm.is_valid:
            userForm.save()
            profileForm.save()
            messages.success(request, f'Account updated successfully!')
            return redirect('profile',pk)

    else:
        userForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/editProfile.html', {"userForm":userForm, "profileForm":profileForm, "profileForm":profileForm})