from django.shortcuts import render
from .models import *



def home(request):
    images = Image.getImages()
    
    return render(request, 'app/home.html', {"images": images})
