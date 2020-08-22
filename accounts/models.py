from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    slug = models.SlugField(blank = True)
    bio = models.CharField(max_length=255, blank=True)
    image = models.ImageField(default = 'default.png',upload_to="profiles")
    cover_image = models.ImageField(default = 'default_cover.png',upload_to="cover_images")
    
    def __str__(self):
        return f'{self.user.username} - Profile'
    
    # def save(self,*args,**kwargs):
    #     super(Profile,self).save(*args,**kwargs)
    #     self.slug = slugify(self.user)
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        self.slug = slugify(self.user)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)         