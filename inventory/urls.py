from django.urls import path
from .views import clothing_item_list, clothing_item_create,home

urlpatterns = [
    path('',home, name=""),
    path('items', clothing_item_list, name='item_list'),
    path('items/create', clothing_item_create, name='item_create'),
]
