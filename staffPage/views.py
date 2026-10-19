from django.shortcuts import render,redirect
from django.urls import reverse
from products.models import Products

# Create your views here.
def staffView(request):
    if(request.user.is_staff == False):
        return redirect(reverse("home"))
    else:
        prod = Products.objects.filter(count__lte = 3)
        return render(request,"staff/staff_view.html",{"prod":prod})