from django.contrib import admin

from .models import TaskStatus
from .models import Subject
from .models import Student
from .models import SubjectStudent
from .models import Task

admin.site.register(TaskStatus)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(SubjectStudent)
admin.site.register(Task)