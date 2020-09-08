from django.shortcuts import render
from .forms import NewsletterUserSignUpForm, NewsletterCreationForm
from .models import NewsletterUser, Newsletter
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def control_newsletter_list(request):
    newsletters = Newsletter.objects.all()
    paginator = Paginator(newsletters, 10)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >=5 else 0
    end_index = index +5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    context = {
        'items':items,
        'page_range':page_range
    }

    template = "conrol_panel/control_newsletter_list.html"

    return render(request, template, context)



def control_newsletter(request):
    form = NewsletterCreationForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        newsletter = Newsletter.objects.get(id = instance.id)
        if newsletter.status == "Published":
            subject = newsletter.subject
            body = newsletter.body
            from_email = settings.EMAIL_HOST_USER
            for email in newsletter.email.all():
                send_mail(subject=subject, from_email=from_email, recipient_list = [email], message=body, fail_silently=True)

    context = {
        'form':form
    }
    template = 'control_panel/control_newsletter.html'
    return render(request, template, context)




# def newsletter_signup(request):
#     form = NewsletterUserSignUpForm(request.POST or None)
#     if form.is_valid():
#         print('form valid')
#         instance = form.save(commit=False)
#         print('commit')
#         if NewsletterUser.objects.filter(email=instance.email).exists():
#             print('sorry this email already exists')
#             instance.save()
#     else:
#         print('form not ')
#     context = {'form':form}
#     template = 'newsletters/sign_up.html'
#     return render(request, template, context)



def newsletter_signup(request):
    pass
    # form = NewsletterUserSignUpForm(request.POST or None)
    # if form.is_valid():
    #     print('form valid')
    #     email = request.POST.get('email')

    #     newsletter = NewsletterUser(email=email)

    #     # newsletter.save()
    #     # instance = form.save(commit=False)
    #     print('commit is false')
    #     if NewsletterUser.objects.filter(email=email).exists():
    #         print('sorry this email already exists')
    #     else:
    #         print('about to be saved cause does not exist')
    #         newsletter.save()
    # else:
    #     print('form not ')
    # context = {'form':form}
    # template = '.html'
    # return render(request, template, context)






def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'your email has been removed from our mailing list', "alert alert-success alert-dismissible")
        else:
            messages.warning(request, 'This email was never on our mailing List', "alert alert-warning alert-dismissible")
            subject = "We are sad to see you Go"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            # subscription_message = "We are sad to see you Go Please Let Us Know if there was any issue with our service" 
            # send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=subscription_message, fail_silently=False)
 
            with open(settings.BASE_DIR + "/templates/newsletters/unsubscribe_email.txt") as f:
                subscription_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=subscription_message, from_email=from_email, to=to_email)
            print('asigning html template')
            html_template = get_template("newsletters/unsubscribe.html").render()
            print('attaching html template')

            message.attach_alternative(html_template, "text/html ")
            print('sending html template')

            message.send()

    context = {'form':form}
    template = 'newsletters/unsubscribe.html'
    return render(request, template, context)



def blog_newsletter_signup(request):
    if form.is_valid():
        print('form valid')
        email = request.POST.get('email')

        newsletter = NewsletterUser(email=email)

        # newsletter.save()
        # instance = form.save(commit=False)
        print('commit is false')
        if NewsletterUser.objects.filter(email=email).exists():
            print('sorry this email already exists')
        else:
            print('about to be saved cause does not exist')
            newsletter.save()
    else:
        print('form not ')
    context = {'form':form}
    template = 'blog_sign_up.html'
    return render(request, template, context)