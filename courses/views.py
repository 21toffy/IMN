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

# def NewModuleView(request, id):
#     course = get_object_or_404(Course,  id=id)
#     form = ModuleForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         new_module=form.save(commit=False)
#         new_module.course=course
#         new_module.save()
#         return redirect('lms:course_list')
#     return render(request, 'lms/new_module.html', context = {'form':form, 'course':course})



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

    
    pass




@login_required
def course_register(request):
    course_id = request.POST.get('selected_course_id')
    course_selected = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form1 = UserCourseForm(request.POST)
        form2 = CourseForm(request.POST, instance=course_selected)
        if request.user.is_authenticated():
            form1.user = request.user
            if form2.is_valid():
                form2.save()
                return render(request, 'template_folder/payment.html', {'email':request.user.email, 'price':form2.price})
            else:
                return HttpResponse('Sorry refresh page and try again!!')
    else:

        form1 = UserCourseForm(request.POST)
        form2 = CourseForm(request.POST, instance=course_selected)
    context = {
        'form1':form1,
        'form2':form2
    }
    return render(request, 'template_folder/register_course.html', context)

    




