from django.db import models

class TaskStatus(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.status}"