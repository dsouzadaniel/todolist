# from django.views.generic.list import ListView
from django.http import HttpResponse


# Create your views here.

def HomePageView(request):
    return HttpResponse("Hello World!")
