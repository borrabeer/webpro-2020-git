from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def manage_page(request, teacher_id):
    return HttpResponse('This is managing page for teacher ID : %d' %teacher_id)
