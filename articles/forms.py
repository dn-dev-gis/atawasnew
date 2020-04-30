from django.forms import ModelForm
from .models import NewsletterSubscriber, AwacRegistration


class SubscribeForm(ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']


class AwacRegistrationForm(ModelForm):
    class Meta:
        model = AwacRegistration
        fields = ['name', 'organisation', 'position', 'email', 'phone', 'atawasmember', 'organisationatawasmember', 'exhibitor']
