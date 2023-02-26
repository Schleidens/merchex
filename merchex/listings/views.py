from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Resources
from listings.forms import contactForm
from django.shortcuts import redirect
from django.core.mail import send_mail

# Create your views here.

def resources(request):
    resources = Resources.objects.all()
    return render(request, 'resources.html', {'resource': resources})

def homePage(request):
    bands = Band.objects.all()
    return render(request, 'band.html', {'band': bands})

def band_details(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'band_details.html', {'band' : band})

def contact_form(request):
    if request.method == 'POST':
        form =  contactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'message from {form.cleaned_data["name"] or "Anonym"}',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=['admin@django.com']
                )
            return redirect('homePage')
    else:
        form = contactForm()
    return render(request, 'contact.html', {'form': form})
