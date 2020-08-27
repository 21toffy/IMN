from django.urls import include, path
from . import views


app_name='blog'


urlpatterns = [

    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
