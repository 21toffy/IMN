from django.urls import path
from .views import newsletter_signup, newsletter_unsubscribe, blog_newsletter_signup
# 
# 

app_name='newsletters'

urlpatterns = [
    path('subscribe/', newsletter_signup, name="newsletter_signup"),
    path('unsubscribe/', newsletter_unsubscribe, name="newsletter_unsubscribe"),
    path('blog-subscribe/', blog_newsletter_signup, name="blog_newsletter_signup"),

]