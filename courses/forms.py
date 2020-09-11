from django import forms
from django.forms import TextInput
from .models import UserCourse, Course



class CourseForm(forms.ModelForm):
    class Meta:
        model =  Course
        fields = ['name', 'price']
        widgets = {
            'name': TextInput(attrs={'readonly': 'readonly'}),
            'price': TextInput(attrs={'readonly': 'readonly'})
        }


class UserCourseForm(forms.ModelForm):
    class Meta:
        model =UserCourse
        fields = ['user']
        widgets = {
            'user': TextInput(attrs={'readonly': 'readonly'})
        }