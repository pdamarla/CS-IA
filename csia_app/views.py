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

@login_required
def adminhomepageview(request):
    subjects=Subject.objects.all()
    context={"subjects":subjects}
    return render(request,"adminhomepage.html",context)


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


def savetask(request, task_id):
    task = get_object_or_404(Task, pk = task_id)
    file = request.FILES["task-file"]
    task.file = file
    task_status = TaskStatus(status = "Submitted")
    task_status.save()
    task.status = task_status
    task.save()
    return redirect('userhomepage')

@login_required
def createtask(request):
    if request.method == "POST":
        subject_id=request.POST["subject"]
        subject=get_object_or_404(Subject,pk =subject_id)
        subject_students=SubjectStudent.objects.filter(subject=subject)
        for ss in subject_students:
            task=Task()
            task.name=request.POST["name"]
            task.description=request.POST["description"]
            task.deadline=request.POST["deadline"]
            taskstatus=TaskStatus()
            taskstatus.status="Pending"
            taskstatus.save()
            task.status=taskstatus
            task.student=ss.student
            task.subject=subject
            task.file=None
            task.grade=0
            task.save()
    return redirect("adminhomepage")

def admintasksview(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    tasks = Task.objects.filter(subject=subject)
    context = {
        "subject": subject, "tasks": tasks
    }
    return render(request, "admintasks.html", context)

def updategrade(request):
    task_id = request.POST["task_id"]
    task = get_object_or_404(Task, pk=task_id)
    grade = int(request.POST["grade"])
    task.grade = grade
    task.save()
    return redirect("adminhomepage")

@login_required
def updatetask(request):
    task_id = request.POST["task_id"]
    task = get_object_or_404(Task, pk=task_id)
    grade = int(request.POST["grade"])
    name = request.POST["name"]
    description = request.POST["description"]
    deadline = request.POST["deadline"]
    task.name = name
    task.description = description
    task.deadline = deadline
    task.grade = grade
    task.save()
    return redirect("adminhomepage")

@login_required
def deletetask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("adminhomepage")


