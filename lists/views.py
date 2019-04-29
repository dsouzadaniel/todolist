from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponse

from .models import List


# Create your views here.

class HomePageView(ListView):
    model = List
    template_name = 'list_list_homepage.html'


class ListDetailView(DetailView):
    model = List
    template_name = 'list_detail.html'
