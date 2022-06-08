from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile/')
    bio = models.TextField(max_length=500, blank=True, default=f'New to gramClone')
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    following = models.ManyToManyField(User, blank=True, related_name='following')


    def __str__(self):
        return f'{self.user.username} profile'

    # def get_absolute_url(self):
    #     return reverse('feed')

    # overriding model's save method by passing pass *args and **kwargs
    def save(self, *args,**kwargs):
        super(Profile, self).save(*args,**kwargs)
 
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size=(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def save_profile(self):
        self.save()


    def delete_profile(self):
        self.delete()

    def update_bio(self, new_bio):
        self.bio = new_bio
        self.save()

    def update_image(self,user_id, new_image):
        user = User.objects.get(id=user_id)
        self.photo = new_image
        self.save() 


        
    def update_image(self, user_id, new_image):
        user = User.objects.get(id = user_id)
        self.photo = new_image 
        self.save()  

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


'''

Django Signal are inside the signal.py file

'''


    

    
   
    
    
