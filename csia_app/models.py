from django.db import models
from django.contrib.auth.models import User

class TaskStatus(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.status}"


class Subject(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     name = models.CharField(max_length=20)
     username = models.CharField(max_length=20)
     email = models.EmailField

     def __str__(self):
         return f"{self.name}, {self.username}"

class SubjectStudent(models.Model):
     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
     student = models.ForeignKey(Student, on_delete=models.CASCADE)

     def __str__(self):
         return f"{self.subject}, {self.student}"

class Task(models.Model):
     name = models.CharField(max_length=100)
     description = models.TextField()
     deadline = models.DateTimeField()
     status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
     student = models.ForeignKey(Student, on_delete=models.CASCADE)
     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
     file = models.FileField(upload_to= "static/", null=True, blank=True)
     grade = models.IntegerField(null=True)

     def __str__(self):
         return f"{self.name}, {self.deadline}, {self.subject}"
