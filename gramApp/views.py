from django.shortcuts import render
from .models import *
# from ..users.forms import UserRegistrationForm



def feed(request):
    images = Image.getImages()
    
    return render(request, 'app/feed.html', {"images": images})

# def home(request):
#     form = UserRegistrationForm
#     return render(request, 'app/home.html', {"form": form})
