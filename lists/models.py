from django.db import models


# Create your models here.

class List(models.Model):
    list_name = models.TextField()

    def __str__(self):
        return str(self.list_name)


class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    item = models.CharField(max_length=140)

    def __str__(self):
        return str(self.item)
