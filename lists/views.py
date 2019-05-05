from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import List, Item


# Create your views here.

class HomePageView(ListView):
    model = List
    template_name = 'list_list_homepage.html'


class ListDetailView(DetailView):
    model = List
    template_name = 'list_detail.html'


class ListCreateView(CreateView):
    model = List
    template_name = 'list_create.html'
    fields = ['list_name']


class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'item_update.html'
    fields = ['item_name']

    def get_success_url(self):
        return reverse_lazy('list_detail', args=[self.kwargs['list_id']])


class ItemCreateView(CreateView):
    model = Item
    template_name = 'item_create.html'
    fields = ['item_name']

    def form_valid(self, form):
        form.instance.list_id = self.kwargs['list_id']
        return super(ItemCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_detail', args=[self.kwargs['list_id']])
