from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile/')
    bio = models.TextField(max_length=500, blank=True, default=f'New to gramClone')
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'

    # def save_profile
    # def delete_profile
    # def update_bio
    # def update_image
