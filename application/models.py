from django.db import models




class Training (models.Model):
    name  = models.CharField(max_length=20)
    price = models.IntegerField()
    about = models.TextField()


class Testimonials(models.Model):
    Name  = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='logos')
    text  = models.TextField()


class TrainingFeatures (models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    feature = models.CharField(max_length=50)


class Blog (models.Model):
    title = models.CharField(max_length=50)
    # author = models.Fore
    image = models.ImageField(upload_to='blog-images')
    content = models.TextField()

class OtherBlogImage (models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='other-blog-images')