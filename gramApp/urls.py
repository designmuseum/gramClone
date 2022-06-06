from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import feedDetailView, PostDetailView,ImageCreateView,ImageDeleteView, ImageUpdateView, ImageDetailView, ImageCreateView #,ImageListView

urlpatterns = [
    # path('', views.home, name='home'),
    path('image-detail/<int:pk>/', PostDetailView.as_view(), name='postDetail'),
    # path('image-detail/<int:pk>/', views.feedView, name='postDetail'),
    # path('image-detail/<int:pk>/', ImageDetailView.as_view(), name='postDetail'),
    path('image/new/', ImageCreateView.as_view(), name='image-create' ),
    path('image/update/<int:id>/', ImageUpdateView.as_view(), name='image-update' ),
    path('image/delete/<int:pk>/', ImageDeleteView.as_view(), name='image-delete' ),
    path('feed/', feedDetailView.as_view(), name='feed'),
    # path('feed-d/', feedDetailView.as_view(), name='feed-detail'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)