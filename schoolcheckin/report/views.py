from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def report_course(request, course_id):
    return HttpResponse('This is report course page of course ID : %d' %course_id)