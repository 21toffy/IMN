from django.db import models
from django.conf import settings



class Course (models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    price = models.IntegerField(default=15)
    def __str__ (self):
        return self.name

    
class UserCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paystack_ref_id = models.CharField(max_length=50)
    user_training_id = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username + self.course
