from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

# Create your views here.

def hello(request):
    return HttpResponse('<h1>Im new to Django</h1>')

def homePage(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
    <h1>I'm the HomePage</h1>
    <br />
    <h2>Here a list pf group</h2>
    <ul>
    <li>{bands[0].name}</li>
    <li>{bands[1].name}</li>
    </ul>
    """)    
