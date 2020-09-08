from django.urls import include, path
from controlpanel import views

from newsletters.views import control_newsletter, control_newsletter_list

app_name='controlpanel'


urlpatterns = [

    path('newsletter',control_newsletter, name='control_newsletter'),
    path('newsletter-list',control_newsletter_list, name='control_newsletter_list '),

]
