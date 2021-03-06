from django.urls import include, path
from . import views


app_name='myapp'


urlpatterns = [

    path('',views.home, name='home'),
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]



