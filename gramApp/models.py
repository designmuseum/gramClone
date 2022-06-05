from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    caption = models.TextField()
    uploadDate = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.caption

    # def save(self):
    #     super().save()
    
    def get_absolute_url(self):
        return reverse('feed')

    
    @classmethod
    def getImages(cls):
        allImages = cls.objects.all()
        return allImages

    
# Profile model is in users app, model.py file