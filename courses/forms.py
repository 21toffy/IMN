from django import forms
from django.forms import TextInput
from .models import UserCourse, Course


class UserCourseForm(forms.ModelForm):
    class Meta:
        model =UserCourse
        fields = ['user']


class CourseForm(forms.ModelForm):
    class Meta:
        model =  Course
        fields = ['name', 'price']

