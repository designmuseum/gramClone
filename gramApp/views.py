from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


@login_required
def feed(request):
    images = Image.getImages()
    
    return render(request, 'app/feed.html', {"images": images })

class ImageView(ListView):
    model = Image
    template_name = 'app/feed.html'
    context_object_name = 'images'
    ordering =['-uploadDate'] 


@login_required
def addPost(request):
    
    return render(request, 'app/home.html')