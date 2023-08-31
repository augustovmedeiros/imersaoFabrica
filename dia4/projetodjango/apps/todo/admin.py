from django.contrib import admin
from apps.todo.models import Task
from apps.users.models import User

admin.site.register(Task)
admin.site.register(User)