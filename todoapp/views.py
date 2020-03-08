from .models import ToDo, Task
from .serializers import TodoSerializer, TaskSerializer
from rest_framework import viewsets


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer