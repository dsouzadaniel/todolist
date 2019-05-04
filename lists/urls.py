from django.urls import path

from .views import HomePageView, ListDetailView, ListCreateView

urlpatterns = [
    path('list/<int:pk>/', ListDetailView.as_view(), name='list_detail'),
    path('list/new/', ListCreateView.as_view(), name='list_create'),
    path('', HomePageView.as_view(), name='home'),
]
