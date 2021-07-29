from django.shortcuts import render
from .forms import signupform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request,'home.html')

def signupuser(request):
    if request.method == 'POST':
        pass
    else:
        fm = signupform()
    return render(request,'signupuser.html',{"form":fm})

def loginuser(request):
    return render(request,'loginuser.html')