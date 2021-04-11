from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('hi django this is my new project')
