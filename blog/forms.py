from django import forms
from django.views.decorators.csrf import csrf_protect
from .models import Contact

class ContactForm(forms.Form):
     class Meta:
          model = Contact