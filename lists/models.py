from django.db import models
from django.urls import reverse


# Create your models here.

class List(models.Model):
    list_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.list_name)

    def get_absolute_url(self):
        return reverse('list_detail', args=[str(self.id)])


class Item(models.Model):
    list = models.ForeignKey(List,
                             on_delete=models.CASCADE,
                             related_name='items')
    item_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.item_name)

    def get_absolute_url(self):
        return reverse('home')
