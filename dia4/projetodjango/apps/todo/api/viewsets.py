from rest_framework import viewsets
from apps.todo.models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

