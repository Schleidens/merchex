from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Resources

# Create your views here.

def hello(request):
    resources = Resources.objects.all()
    return HttpResponse(f"""
    <h1>Im new to Django</h1>
    <br />
    <h2>Here are resources i'm using</h2>
    <ul>
    <ol>{resources[0].title}</ol>
    <ol>{resources[1].title}</ol>
    </ol>
    """)

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
