from django.urls import path
from . import views

urlpatterns = [
    path("add", views.add_item, name="add_item"),
    path("get", views.get_items, name="get_item"),
]