from django.urls import path
from . import views


app_name='courses'


urlpatterns = [

    path('register/', views.course_register, name = "course_register"),
    path('courses/', views.course_list, name = "course_list"),
    path('course/<int:pk>', views.course_detail, name = "course_detail"),

]