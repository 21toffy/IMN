from django.shortcuts import render, get_object_or_404, HttpResponse
from . models import About, Services, Blog, Contact, Clientels, Testimonials, Gallery, Socials
from django.utils import timezone
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)


def home(request):
    print('if blog')
    if Blog:
        blogs=Blog.objects.filter(status=0).order_by('-time')[:3]
        print(blogs)
    
    

    context={

        'blogs':blogs,

    }

    return render(request, 'index.html', context)



class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Blog
    context_object_name='posts'

    ''' Returns  the list of views for this View'''
    def get_queryset(self):
        return Blog.objects.filter(time__lte=timezone.now()).order_by('-time')  #__lte is less than equals too!

class PostDetailView(DetailView):
    model = Blog
    context_object_name='post_detail'
    
    # def get_context_data(self, **kwargs):
    #     context = super(RoomView, self).get_context_data(**kwargs)
    #     context['workers'] = Worker.objects.all()
    #     print context
    #     return context

    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['blog_list'] = Blog.objects.filter(time__lte=timezone.now()).order_by('-time')[0:10]
        return context

    # def get_queryset(self):
    #     return Blog.objects.filter(time__lte=timezone.now()).order_by('-time')
    
def contact(request):
    return render(request, 'contact.html')


