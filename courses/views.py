from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CourseForm, UserCourseForm
from .models import Course, UserCourse


def course_list(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    template = 'courses/course_list.html'
    return render(request, template, context)
    

def course_detail (request, id):
    course = get_object_or_404(Course,  id=id)
    # if request.user.is_authenticated():

    context = {'course':course}
    template = 'courses/course_detail.html'
    return render(request, template, context)

# on the course detail page(check course_detail.html) when you click on proceed to payment the button is a form that passes the course id to a course_register view(check courses/views.py) to get the details of the selected  course to the course register view, this view is supposed to display an already filled form(check courses/forms.py), filled with the logged in user (request.user), course price, course name and a button to pass these details to paystack(check template/register_course.html) but the problem is that when you click on the proceed to payment button in the course detail page the course register page does not display any form as i want it to but it rather posts an empty form


@login_required
def course_register(request, id):
    course_id = request.POST.get('selected_course_id')
    course_selected = get_object_or_404(Course, id=course_id)
    print('-------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------')
    u_form = UserCourseForm(instance=request.user)
    c_form = CourseForm(instance=course_selected)
    if request.method == 'POST':
        # print('request is post')
        u_form = UserCourseForm(request.POST, instance=request.user)
        c_form = CourseForm(request.POST, instance=course_selected)
        print(u_form)
        print(c_form)
        
        if u_form.is_valid() and c_form.is_valid():
            print('valid data')
            u_form.save()
            c_form.save()

            return render(request, 'courses/payment.html', {'email':request.user.email, 'price':c_form.price})
        else:
            return HttpResponse('Sorry refresh page and try again!!')
    else:
        u_form = UserCourseForm(instance=request.user)
        c_form = CourseForm(instance=course_selected)
    context = {
        'u_form':u_form,
        'c_form':c_form
    }
    return render(request, 'courses/register_course.html', context)

    




