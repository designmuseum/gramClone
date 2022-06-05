from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import ImageListView, ImageDetailView

urlpatterns = [
    # path('', views.home, name='home'),
    # path('feed/', views.feed, name='feed'),
    path('feed/', ImageListView.as_view(), name='feed'),
    path('post-detail/<int:pk>/', ImageDetailView.as_view(), name='postDetail')


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)