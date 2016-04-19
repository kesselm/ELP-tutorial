from django.shortcuts import render_to_response

from courses.models import Course

def course_list(request):
    courses = Course.objects.all()
    return render_to_response('courses/list.html', {'courses':courses})

from django.shortcuts import get_object_or_404, render

def course_detail(request, course_id):
   course = get_object_or_404(Course, pk=course_id)
   return render(request, 'courses/detail.html', {'course': course})