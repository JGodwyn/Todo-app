from django.contrib import admin
from .models import Username, Password, Task


class UsernameDisplay(admin.ModelAdmin):
    list_display = ('Username', 'time_created')


class TaskDisplay(admin.ModelAdmin):
    list_display = ('task', 'time_created', 'time_to_do')


admin.site.register(Username, UsernameDisplay)
admin.site.register(Task, TaskDisplay)
