from django.shortcuts import render, get_object_or_404, HttpResponse
from . models import About, Services, Blog, Contact, Clientels, Testimonials, Gallery, Socials
from django.utils import timezone
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)


def home(request):
    about =About.objects.all()
    services=Services.objects.all()
    blog1=Blog.objects.all()[0]
    blog2=Blog.objects.all()[1]
    contact =Contact.objects.all()
    clientels =Clientels.objects.all()
    testimonials=Testimonials.objects.all()
    gallery=Gallery.objects.all()
    socials=Socials.objects.all().first()

    context={
        'about':about,
        'services':services,
        'blog1':blog1,
        'blog2':blog2,
        'contact':contact,
        'clientels':clientels,
        'testimonials':testimonials,
        'gallery':gallery,
        'socials':socials,
    }

    return render(request, 'index.html', context)



class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Blog
    context_object_name='red'

    ''' Returns  the list of views for this View'''
    def get_queryset(self):
        return Blog.objects.filter(time__lte=timezone.now()).order_by('-time')  #__lte is less than equals too!

class PostDetailView(DetailView):
    model = Blog
    context_object_name='post_detail'
    