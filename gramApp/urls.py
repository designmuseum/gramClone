from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import like, dislike, feedDetailView, PostDetailView,ImageCreateView,ImageDeleteView, ImageUpdateView, ImageDetailView, ImageCreateView #,ImageListView

urlpatterns = [
    path('image/<int:pk>/', PostDetailView.as_view(), name='postDetail'),
    path('image/<int:pk>/like', like.as_view(), name='like'),
    path('image/<int:pk>/dislike', dislike.as_view(), name='dislike'),
    path('image/new/', ImageCreateView.as_view(), name='image-create' ),
    path('image/update/<int:pk>/', ImageUpdateView.as_view(), name='image-update' ),
    path('image/delete/<int:pk>/', ImageDeleteView.as_view(), name='image-delete' ),
    path('feed/', feedDetailView.as_view(), name='feed'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)