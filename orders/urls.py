from django.urls import path
from . import views

urlpatterns = [
    path("add", views.add_order, name="add_order"),
    path("<int:order_id>", views.get_order, name="get_order"),
]