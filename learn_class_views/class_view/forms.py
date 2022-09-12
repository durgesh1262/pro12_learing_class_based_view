from django import forms
class contactform(forms.form):
    name= forms.CharField(max_length=50)
    contact = forms.NumberInput()