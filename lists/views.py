from django.views.generic.detail import DetailView
from django.http import HttpResponse


# Create your views here.

def HomePageView(request):
    return HttpResponse("Hello World!")


class ListDetailView(DetailView):
    pass
