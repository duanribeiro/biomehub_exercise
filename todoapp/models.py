from django.db import models
import uuid

class ToDo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300)
    deadline = models.DateField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300)
    deadline = models.DateField()
    done = models.BooleanField(default=False)
    user = models.CharField(max_length=300)

    todolist = models.ForeignKey(ToDo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title