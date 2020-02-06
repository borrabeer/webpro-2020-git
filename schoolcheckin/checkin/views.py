from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
def show_course(request):
    return render(request, template_name="checkin/index.html", context={'courses':models.courses, 'classes':models.classes, 'attendance':models.attendance})
    
def show_course_detail(request, course_id):
    return render(request, template_name="checkin/course_detail.html", context={'id':course_id, 'courses':models.courses, 'classes':models.classes, 'attendance':models.attendance})

def checking_course(request, course_id):
    return render(request, template_name="checkin/course_detail.html", context={'id':course_id, 'courses':models.courses, 'classes':models.classes, 'attendance':models.attendance})