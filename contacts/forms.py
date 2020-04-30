from django.forms import ModelForm
from .models import Person

class ContactForm(ModelForm):
    class Meta:
        model = Person
        fields = ['organisation', 'lastName', 'firstNames', 'phone1', 'phone2', 'phone3', 'phone4', 'phone5', 'phone6', 'phone7', 'email1', 'email2', 'email3', 'email4', 'email5', 'pobox', 'town', 'country', 'position', 'comment']
