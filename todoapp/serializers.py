from todoapp.models import Task, ToDo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    title = serializers.CharField()

    class Meta:
        model = ToDo
        fields = ('__all__')


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    user = serializers.CharField()
    todolist = serializers.StringRelatedField (many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('__all__')
