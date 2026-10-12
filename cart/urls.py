from django.urls import path
from . import views

urlpatterns = [
    path("view/",views.view_cart,name="view_cart"),
    path("add/<int:pk>",views.add_cart,name="add_cart"),
    path("minus/<int:pk>",views.remove_cart,name="minus_cart"),
    path("buy_one/<int:pk>",views.buy_one_cart,name="buy_one_cart"),
    path("buy_all",views.buy_all_cart,name="buy_all_cart"),
]
