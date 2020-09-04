from django.shortcuts import render
from .forms import NewsletterUserSignUpForm
from .models import NewsletterUser
from django.contrib import messages


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