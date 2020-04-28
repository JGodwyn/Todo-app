from django.db import models
from django.utils import timezone
import datetime



class Username(models.Model): # for the Usernames
    Username = models.CharField(max_length = 100)
    time_created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.Username


class Password(models.Model): # for their individual passwords
    Username_link = models.ForeignKey(Username, on_delete = models.CASCADE, related_name = 'password')
    Password = models.CharField(max_length = 100)

    def __str__(self):
        return self.Password


class Task(models.Model): # for their task
    Tasks_link = models.ForeignKey(Username, on_delete = models.CASCADE, related_name = 'tasks')
    task = models.TextField()
    time_created = models.DateTimeField(auto_now = True)
    time_to_do = models.DateTimeField(default = timezone.now() + datetime.timedelta(days = 1))

    def __str__(self):
        return self.task
