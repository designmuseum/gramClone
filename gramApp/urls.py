from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import ImageCreateView, ImageUpdateView,ImageListView, ImageDetailView, ImageCreateView

urlpatterns = [
    # path('', views.home, name='home'),
    # path('feed/', views.feed, name='feed'),
    path('feed/', ImageListView.as_view(), name='feed'),
    path('image-detail/<int:pk>/', ImageDetailView.as_view(), name='postDetail'),
    # path('image/new/', views.newImage, name='image-create' ),
    path('image/new/', ImageCreateView.as_view(), name='image-create' ),
    path('image/update/<int:pk>/', ImageUpdateView.as_view(), name='image-update' ),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)