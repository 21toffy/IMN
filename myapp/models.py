from django.db import models

from django.conf import settings

from django.urls import reverse

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from django.contrib.auth.models import User



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




# @receiver(pre_delete, sender=(Blog,Clientels,Gallery))
# def photo_delete(sender, instance, **kwargs):
#     cloudinary.uploader.destroy(instance.image.public_id)