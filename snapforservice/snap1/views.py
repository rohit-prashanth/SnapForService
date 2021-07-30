from django.shortcuts import render
from .forms import SignupForm, UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import UserProfileTable

# Create your views here.

def home(request):
    return render(request,'home.html')

def signupuser(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Congratulations!, You have Successfully Signed-up!!")
            return HttpResponseRedirect('/')
    else:
        fm = SignupForm()
        return render(request,'signupuser.html',{"form":fm})

def loginuser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pwd = fm.cleaned_data['password']
                user = authenticate(username=uname,password=pwd)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/userprofile/')
        else:
            fm = AuthenticationForm()
            return render(request,'loginuser.html',{'form':fm})
    else:
        return HttpResponseRedirect('/userprofile/')


def userprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserProfileForm(request.POST)
            if fm.is_valid():
                new_form = fm.save(commit=False)
                new_form.user_id = request.user
                new_form.save()
                return HttpResponseRedirect('/userprofile/')
        else:
            fm = UserProfileForm()
            data = UserProfileTable.objects.all()
            print(data)
            return render(request, 'userprofile.html', {'form': fm, 'data': data})
    else:
        return HttpResponseRedirect('/login/')

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/')

def delete_data(request,id):
    if request.method == "POST":
        row = UserProfileTable.objects.get(pk=id)
        row.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == 'POST':
        data = UserProfileTable.objects.get(pk=id)
        form = UserProfileForm(request.POST, instance=data)
        form.save()
        messages.info(request,'Updated Successfully')
        return HttpResponseRedirect('/')
    else:
        data = UserProfileTable.objects.get(pk=id)
        form = UserProfileForm(instance=data)
        return render(request,'update.html',{'form':form})