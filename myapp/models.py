from django.db import models

from django.conf import settings

from django.urls import reverse

class About(models.Model):
    about=models.TextField(null=True, blank=True)
    vission=models.CharField(max_length=100, null=True, blank=True)
    mission=models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.about[0:100]

  
class Services(models.Model):
    icon=models.FileField(upload_to="icons", null=True, blank=True)
    title=models.CharField(max_length=25, null=True, blank=True)
    text=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title=models.CharField(max_length=25)
    text=models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    img1=models.FileField(upload_to='blog_images')
    img2=models.FileField(upload_to='blog_images', null=True, blank=True)
    img3=models.FileField(upload_to='blog_images', null=True, blank=True)

    def __str__(self):
        return self.title
        

    def get_absolute_url(self):
        return reverse('myapp:post_detail', kwargs={'pk': self.id})


class Gallery(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, default='default.jpg')
    images = models.FileField(upload_to='gallery_image')
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
    logo = models.FileField(upload_to='client_logos')
    def __str__(self):
        return self.name



class Testimonials(models.Model):
    text=models.CharField(max_length=50)
    def __str__(self):
        return self.text[:20]


class Socials(models.Model):
    facebook=models.URLField(null=True, blank=False)
    instagram=models.URLField(null=True, blank=False)
    twitter = models.URLField(null=True, blank=False)
    youtube = models.URLField(null=True, blank=False)