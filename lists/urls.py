from django.urls import path

from .views import HomePageView, ListDetailView

urlpatterns = [
    path('list/<int:pk>/', ListDetailView.as_view(), name='list_detail'),
    path('', HomePageView, name='home'),
]
