from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime
from PIL import Image


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='uploads/images',
                                  default="default.jpg")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        
    def __str__(self):
        return self.title

    def body_snippet(self):
        return self.body[:110] + '...'

    def title_snippet(self):
        if (len(self.title) >= 30):
            return self.title[:30] + '...'
        else:
            return self.title
        
    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"slug": self.slug})
    
