from django.shortcuts import render



def course_list(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    template = 'course/course_list.html'
    return render(request, template, context)
    

def course_detail (request, pk):
    
    pass



def course_register(request):
    pass





