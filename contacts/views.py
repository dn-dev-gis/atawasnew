from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ContactForm
from .models import Person

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'contactdb/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('contactall')
            except IntegrityError:
                return render(request, 'contactdb/signupuser.html', {'form':UserCreationForm(), 'error':'User already exists'})
        else:
            return render(request, 'contactdb/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def contactall(request):
    allcontacts = Person.objects.all()
    return render(request, 'contactdb/contact_all.html',{'allcontacts':allcontacts})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'contactdb/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'contactdb/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password do not match'})
        else:
            login(request, user)
            return redirect('contactall')

def home(request):
    return render(request, 'contactdb/home.html')

def createcontact(request):
    if request.method == 'GET':
        return render(request, 'contactdb/createcontact.html', {'form':ContactForm()})
    else:
        form = ContactForm(request.POST)
        newcontact = form.save(commit=False)
        newcontact.user = request.user
        newcontact.save()
        return redirect('contactall')
