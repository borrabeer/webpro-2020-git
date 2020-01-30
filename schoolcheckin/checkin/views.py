from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_course(request, teacher_id):
    return HttpResponse('This is course page of Teacher ID : %d' %teacher_id)
    
def show_course_detail(request, teacher_id, course_id):
    return HttpResponse('This is course page of Teacher ID : %d <br> You are in course ID : %d' %(teacher_id, course_id))

def checking_course(request, course_id):
    return HttpResponse('You are checking in course ID : %d' %(course_id))