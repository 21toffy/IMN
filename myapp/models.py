from django.db import models

from django.conf import settings

from django.urls import reverse

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from django.contrib.auth.models import User


class About(models.Model):
    about=models.TextField(null=True, blank=True)
    vission=models.CharField(max_length=100, null=True, blank=True)
    mission=models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.about[0:100]

  
class Services(models.Model):
    icon=models.ImageField(upload_to='services/',null=True, blank=True)
    title=models.CharField(max_length=25, null=True, blank=True)
    text=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

CATEGORY = (
    ("Event","Event"),
    ("Training","Training"),
    ("Blog Post","Blog Post"),
    ("Tutorial","Tutorial"),
)

class Blog(models.Model):
    title=models.CharField(max_length=25)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')

    text=models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    landing_image=models.ImageField(upload_to='blog_images/',null=True, blank=True)
    img2=models.ImageField(upload_to='blog_images/',null=True, blank=True)
    img3=models.ImageField(upload_to='blog_images/',null=True, blank=True)
    img4=models.ImageField(upload_to='blog_images/',null=True, blank=True)
    img5=models.ImageField(upload_to='blog_images/',null=True, blank=True)
    img6=models.ImageField(upload_to='blog_images/',null=True, blank=True)
    vid=models.FileField(upload_to='blog_video/',null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.CharField(choices=CATEGORY, max_length=20, default="Event")
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.title
        

    def get_absolute_url(self):
        return reverse('myapp:post_detail', kwargs={'pk': self.id})


class Gallery(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, default='default.jpg')
    blog_images = models.ImageField()
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
    logo = models.ImageField()
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


# @receiver(pre_delete, sender=(Blog,Clientels,Gallery))
# def photo_delete(sender, instance, **kwargs):
#     cloudinary.uploader.destroy(instance.image.public_id)