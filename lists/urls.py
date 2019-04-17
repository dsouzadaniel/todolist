from django.urls import path

from .views import HomePageView, ListDetailView

urlpatterns = [
    path('', HomePageView, name='home'),
    path('list/<int: pk>/', ListDetailView.as_view(), name='list_detail')

]