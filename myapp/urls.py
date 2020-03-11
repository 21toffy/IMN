from django.urls import include, path
from myapp import views


app_name='myapp'


urlpatterns = [

    path('',views.home, name='home')
]

