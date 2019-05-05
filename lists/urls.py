from django.urls import path

from .views import HomePageView, ListDetailView, ListCreateView, ItemUpdateView, ItemCreateView

urlpatterns = [
    path('list/<int:list_id>/item/<int:pk>', ItemUpdateView.as_view(), name='item_update'),
    path('list/<int:list_id>/item/new/', ItemCreateView.as_view(), name='item_create'),
    path('list/<int:pk>/', ListDetailView.as_view(), name='list_detail'),
    path('list/new/', ListCreateView.as_view(), name='list_create'),
    path('', HomePageView.as_view(), name='home'),
]
