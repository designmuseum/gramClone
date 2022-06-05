from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import ImageView

urlpatterns = [
    # path('', views.home, name='home'),
    # path('feed/', views.feed, name='feed'),
    path('feed/', ImageView.as_view(), name='feed'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)