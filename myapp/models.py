from django.db import models

from django.conf import settings

from django.urls import reverse
from cloudinary.models import CloudinaryField

from django.db.models.signals import pre_delete
from django.dispatch import receiver

import cloudinary


class About(models.Model):
    about=models.TextField(null=True, blank=True)
    vission=models.CharField(max_length=100, null=True, blank=True)
    mission=models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.about[0:100]

  
class Services(models.Model):
    icon=CloudinaryField(null=True, blank=True)
    title=models.CharField(max_length=25, null=True, blank=True)
    text=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title=models.CharField(max_length=25)
    text=models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    img1=CloudinaryField()
    img2=CloudinaryField(null=True, blank=True)
    img3=CloudinaryField(null=True, blank=True)
    vid=CloudinaryField(null=True, blank=True)

    def __str__(self):
        return self.title
        

    def get_absolute_url(self):
        return reverse('myapp:post_detail', kwargs={'pk': self.id})


class Gallery(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, default='default.jpg')
    images = CloudinaryField()
    def __str__(self):
        return self.blog

class Contact(models.Model):
    name=models.CharField(max_length=25,default='tofunmi')
    phone=models.CharField(max_length=11)
    email=models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

class Clientels(models.Model):
    name=models.CharField(max_length=25)
    logo = CloudinaryField()
    def __str__(self):
        return self.name



class Testimonials(models.Model):
    text=models.CharField(max_length=150)
    def __str__(self):
        return self.text[:20]


class Socials(models.Model):
    facebook=models.URLField(null=True, blank=False)
    instagram=models.URLField(null=True, blank=False)
    twitter = models.URLField(null=True, blank=False)
    youtube = models.URLField(null=True, blank=False)


@receiver(pre_delete, sender=(Blog,Clientels,Gallery))
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)