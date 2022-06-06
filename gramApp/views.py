from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView, ListView, UpdateView,DetailView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import commentForm
from django.views.generic import View



# @method_decorator(login_required, name='dispatch')
class ImageListView(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'app/feed.html'
    context_object_name = 'images'
    ordering =['-uploadDate'] 
    

# class CommentCreateView( LoginRequiredMixin, CreateView):
#     model = imgComment
#     fields=['comment']
#     template_name = 'app/feed.html'    
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)







# @method_decorator(login_required, name='dispatch')
class ImageDetailView(LoginRequiredMixin, DetailView):
    model = Image
    template_name = 'app/ImgDetail.html'    
    context_object_name = 'image'

# @method_decorator(login_required, name='dispatch')
class ImageCreateView( LoginRequiredMixin, CreateView):
    model = Image
    fields=['image', 'caption']
    template_name = 'app/newImage.html'    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




# @method_decorator(login_required, name='dispatch')
class ImageUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView,):
    model = Image
    fields=['caption']
    template_name = 'app/updateImage.html'    
    # success_url = '/feed/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Prevents other users from editing other people's images
    def test_func(self):
        image = self.get_object()
        if self.request.user == image.author:
            return True
        return False
        # else:
        #     return render('users/feed')

        
class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Image
    template_name = 'app/confirmDelete.html'    
    context_object_name = 'image'
    success_url = '/feed/'

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.author:
            return True
        return False


class feedDetailView(View):
    def get(self, request, *args, **kwargs):
        images = Image.getImages
        form = commentForm()
        
        return render(request, 'app/feed.html', {'images': images, 'form': form})
    def post(self, request, *args, **kwargs):
        pass