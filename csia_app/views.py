from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
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


@login_required
def userhomepageview(request):
    username = request.user.username

    student = Student.objects.get(user = request.user)
    subjects = []
    student_subjects = SubjectStudent.objects.filter(student = student)
    for ss in student_subjects:
        subjects.append(ss.subject)
    context = {
        "username": username,
        "subjects": subjects
    }
    return render(request, "userhomepage.html", context)


def userlogout(request):
    logout(request)
    return redirect('userlogin')

def usertasksview(request, subject_id):
    subject = get_object_or_404(Subject, pk = subject_id)
    student = Student.objects.get(user=request.user)
    tasks = Task.objects.filter(subject = subject, student = student)
    context = {
        "subject": subject, "tasks": tasks
    }
    return render(request, "usertasks.html", context)
