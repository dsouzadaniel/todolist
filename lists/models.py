from django.db import models


# Create your models here.

class List(models.Model):
    todo_item = models.TextField()

    def __str__(self):
        return str(self.todo_item)
