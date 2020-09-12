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

    



def NewModuleUpdateView(request, id):
    # course = get_object_or_404(Course,  id=id)
    module_to_update = get_object_or_404(Module,  id=id)
    form = ModuleForm(request.POST or None, request.FILES or None, instance = module_to_update)
    if form.is_valid():
        new_module=form.save(commit=False)
        # new_module.course=course
        new_module.save()
        return redirect('lms:course_list')
    return render(request, 'lms/new_module.html', context = {'form':form})
    
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

    




