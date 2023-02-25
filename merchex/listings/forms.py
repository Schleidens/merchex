from  django import forms

class contactForm(forms.Form):
    name =  forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)