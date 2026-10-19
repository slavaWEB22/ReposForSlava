from django.urls import path
from . import views

urlpatterns = [
    path("",views.staffView,name="staff_view")
]
