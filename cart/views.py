from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Cart
from products.models import Products

# Create your views here.
def view_cart(request):

    cart = Cart.objects.all()
    listMessage = []
    for i in cart:
        if i.count > i.prod.count:
            i.count = i.prod.count
            i.save()
            if "Количество товара уменьшелось" not in listMessage:
                listMessage.append("Количество товара уменьшелось")
        if i.prod.count <= 10:
            if "Осталось мало товара" not in listMessage:
                listMessage.append("Осталось мало товара")
    return render(request,"cart/view_cart.html",{"cartLst":cart,"listMessage":listMessage})

def add_cart(request,pk):
    prod = Products.objects.get(id=pk)
    cart,_ = Cart.objects.get_or_create(prod=prod,user=request.user)
    if cart.count != prod.count:
        cart.count += 1
        cart.save()
    return redirect(reverse("view_cart"))

def remove_cart(request,pk):
    prod = Products.objects.get(id=pk)
    cart = Cart.objects.get(prod=prod)
    if cart.count != 1:
        cart.count -= 1
        cart.save()
    else:
        cart.delete()
    return redirect(reverse("view_cart"))

def buy_one_cart(request,pk):
    prod = Products.objects.get(id=pk)
    cart = Cart.objects.get(prod=prod)
    prod.count -= cart.count
    prod.save()
    cart.delete()
    return redirect(reverse("view_cart"))

def buy_all_cart(request):
    cart = Cart.objects.all()
    for i in cart:
        i.prod.count -= i.count
        i.prod.save()
    cart.delete()
    return redirect(reverse("view_cart"))
