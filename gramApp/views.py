from email.mime import image
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView, ListView, UpdateView,DetailView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import commentForm
from django.views.generic import View


from users.models import Profile
from .models import *


class feedDetailView(LoginRequiredMixin, View):
    def get(self, request ):
        images = Image.getImages().order_by('-uploadDate')
        count = imgComment.objects.count()
        # comments = imgComment.get_comments().count()
        comments=imgComment.objects.filter().count
        suggestedProfiles = Profile.objects.all()
        # form = commentForm()
        if request.method == 'POST':
            form = commentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.author = request.user
                new_comment.image = Image.objects.filter(id=id)
                new_comment.save()
            return redirect('postDetail')
        else:
            form = commentForm()

        return render(request, 'app/feed.html', {'images': images, 'comments': comments,'suggestedProfiles':suggestedProfiles, 'count': count})

# @method_decorator(login_required, name='dispatch')
class ImageListView(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'app/feed.html'
    context_object_name = 'images'
    ordering =['-uploadDate'] 
    




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
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('postDetail', kwargs={'pk': pk})
#Prevents other users from editing other people's images
    def test_func(self):
        image = self.get_object()
        return self.request.user == image.author

        
class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Image
    template_name = 'app/confirmDelete.html'    
    context_object_name = 'image'
    success_url = '/feed/'

    def test_func(self, request, pk, *args, **kwargs):
        image = self.get_object()
        # image = Image.objects.get(pk=pk)
        if self.request.user == image.author:
            return True
        return False


class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        image = Image.objects.get(pk=pk)
        form = commentForm()
        comments = imgComment.objects.filter(image=image).order_by('-createDate')

        context = {
            'image': image,
            'form': form,
            'comments': comments,
        }

        return render(request, 'app/ImgDetail.html', context)

    def post(self, request, pk, *args, **kwargs):
        image = Image.objects.get(pk=pk)
        form = commentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.image = image
            new_comment.save()
        return redirect('feed')
        

class like(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        image = Image.objects.get(pk=pk)

        is_dislike = False

        for dislike in image.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            image.dislikes.remove(request.user)

        is_like = False

        for like in image.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            image.likes.add(request.user)

        if is_like:
            image.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class dislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        image = Image.objects.get(pk=pk)

        is_like = False

        for like in image.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            image.likes.remove(request.user)

        is_dislike = False

        for dislike in image.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            image.dislikes.add(request.user)

        if is_dislike:
            image.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

