from django.db import models

from django.conf import settings



class About(models.Model):
    about=models.TextField(null=True, blank=True)
    vission=models.CharField(max_length=100, null=True, blank=True)
    mission=models.CharField(max_length=100, null=True, blank=True)

class Services(models.Model):
    icon=models.FileField(upload_to="icons")
    title=models.CharField(max_length=25, null=True, blank=True)
    text=models.CharField(max_length=100, null=True, blank=True)

class Blog(models.Model):
    title=models.CharField(max_length=25)
    text=models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    img1=models.FileField(upload_to='/blog_images')
    img2=models.FileField(upload_to='/blog_images', null=True, blank=True)
    img3=models.FileField(upload_to='/blog_images', null=True, blank=True)
    def get_absolute_url(self):
        return reverse('myapp:post_detail', kwargs={'pk': self.id})
    


class Contact(models.Model):
    phone=models.CharField(max_length=11, min_length=11)
    email=models.EmailField(null=True, blank=True)
