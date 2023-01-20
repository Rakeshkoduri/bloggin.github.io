from django.db import models
from django.urls import reverse
from django.contrib.auth.admin import User


# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    product = models.CharField(max_length=1000)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=2000,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})

