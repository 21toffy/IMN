from django.urls import path
from . import views


app_name='courses'


urlpatterns = [

    path('register/', views.course_register, name = "course_register"),
    path('/', views.course_list, name = "course_list"),
    path('/<int:id>/', views.course_detail, name = "course_detail"),

]