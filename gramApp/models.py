from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    caption = models.TextField()
    uploadDate = models.DateTimeField(default=timezone.now)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
    @classmethod
    def getImages(cls):
        allImages = cls.objects.all()
        return allImages


