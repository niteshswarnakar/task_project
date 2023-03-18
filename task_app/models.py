from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length = 180)
    body = models.CharField(max_length = 600)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.title