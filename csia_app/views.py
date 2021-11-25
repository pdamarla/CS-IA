from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def adminloginview(request):
    return render(request,"adminlogin.html")

def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username, password = password)

    # user exists
    if user is not None and user.username=="Murali555":
        login(request,user)
        return redirect ('adminhomepage')
    # user doesnt exists
    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid Username/Password")
        return redirect('adminloginpage')


def adminhomepageview(request):
    return render(request,"adminhomepage.html")


def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')

def userloginview(request):
    return render(request,"userlogin.html")

def homepageview(request):
    return render(request, "homepage.html")

def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    # user exists
    if user is not None:
        login(request, user)
        return redirect('userhomepage')
    # user doesnt exists
    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid Username/Password")
        return redirect('userlogin')


def userhomepageview(request):
    return render(request, "userhomepage.html")


def userlogout(request):
    logout(request)
    return redirect('userlogin')



