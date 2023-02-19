from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Resources

# Create your views here.

def resources(request):
    resources = Resources.objects.all()
    return render(request, 'resources.html', {'resource': resources})

def homePage(request):
    bands = Band.objects.all()
    return render(request, 'band.html', {'band': bands}) 
