from django.urls import include, path
from myapp import views


app_name='myapp'


urlpatterns = [

    path('',views.home, name='home'),
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]

