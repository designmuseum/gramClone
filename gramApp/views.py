from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.utils.decorators import method_decorator


# @login_required
# def feed(request):
#     images = Image.getImages()
    
#     return render(request, 'app/feed.html', {"images": images })


@method_decorator(login_required, name='dispatch')
class ImageListView(ListView):
    model = Image
    template_name = 'app/feed.html'
    context_object_name = 'images'
    ordering =['-uploadDate'] 



@method_decorator(login_required, name='dispatch')
class ImageDetailView(DetailView):
    model = Image
    template_name = 'app/ImgDetail.html'    
    context_object_name = 'image'

@method_decorator(login_required, name='dispatch')
class ImageCreateView(CreateView):
    model = Image
    fields=['image', 'caption']
    template_name = 'app/newImage.html'    
    # context_object_name = 'image'







# @login_required
# def addPost(request):
    
#     return render(request, 'app/home.html')