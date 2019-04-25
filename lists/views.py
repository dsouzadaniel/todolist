from django.views.generic.detail import DetailView
from django.http import HttpResponse

from .models import List


# Create your views here.

def HomePageView(request):
    return HttpResponse("Hello World!")


class ListDetailView(DetailView):
    model = List
    template_name = 'list_detail.html'
