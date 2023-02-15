from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('<h1>Im new to Django</h1>')

def homePage(request):
    return HttpResponse("<h1>I'm the HomePage</h1>")    
