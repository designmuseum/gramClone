from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


@login_required
def feed(request):
    images = Image.getImages()
    ordering =['-uploadDate'] 
    
    return render(request, 'app/feed.html', {"images": images })

# def home(request):
#     form = UserRegistrationForm
#     return render(request, 'app/home.html', {"form": form})
@login_required
def addPost(request):
    
    return render(request, 'app/home.html')