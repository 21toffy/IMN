from django.shortcuts import render, get_object_or_404, HttpResponse
from . models import Blog
from django.utils import timezone
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)

from newsletters.forms import NewsletterUserSignUpForm
from newsletters.models import NewsletterUser

from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages

from django.template.loader import get_template

def home(request):
    print('if blog')
    if Blog:
        blogs=Blog.objects.filter(status=0).order_by('-time')[:3]
    
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        print('form valid')
        email = request.POST.get('email')

        newsletter = NewsletterUser(email=email)

        # newsletter.save()
        # instance = form.save(commit=False)
        print('commit is false')
        if NewsletterUser.objects.filter(email=email).exists():
            messages.warning(request, 'your are already receiving Newsletters from us', "alert alert-warning alert-dismissible")

            print('sorry this email already exists')
        else:
            print('about to be saved cause does not exist')
            newsletter.save()
            messages.success(request, 'your email has been submitted check your inbox', "alert alert-success alert-dismissible")

            subject = "thank you for Joining our NewsLetters"
            from_email = settings.EMAIL_HOST_USER
            to_email = [email]
            # subscription_message = "welcome to Influenz media... if you will like to unsunscribe visit 127  .0.0.1:8000/newsletter/unsubscribe"
            # send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=subscription_message, fail_silently=False)

            with open(settings.BASE_DIR + "/templates/newsletters/sign_up_email.txt") as f:
                subscription_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=subscription_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletters/sign_up_email.html").render()
            message.attach_alternative(html_template, "text/html ")
            message.send()
    else:
        print('form not ')
    # context = {}
    # template = 'index.html'
    # return render(request, template, context)

    context={

        'blogs':blogs,
        'form':form

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
    
def contact(request):
    return render(request, 'contact.html')


