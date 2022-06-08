from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Profile model is in users app, model.py file

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    caption = models.TextField()
    uploadDate = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __str__(self):
        return self.caption

    # def save(self):
    #     super().save()
    
    def get_absolute_url(self):
        return reverse('feed')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()


    @classmethod
    def getImages(cls):
        allImages = cls.objects.all()
        return allImages


    @classmethod
    def getProfileIMages(cls, user_id):
        image = Image.objects.filter(user_id=user_id).all()
        return image
    
class imgComment(models.Model):
    comment = models.TextField()
    createDate = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def updateComment(self, new_comment):
        self.comment = new_comment
        self.save()

    def __str__(self):
        return f'Comment: {self.comment}'

    @classmethod
    def get_comments(cls,id):
            comments = cls.objects.filter(image_id=id)
            return comments     