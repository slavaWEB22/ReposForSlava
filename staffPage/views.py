from django.shortcuts import render,redirect
from django.urls import reverse
from products.models import Products

# Create your views here.


def staffView(request):
    if(request.user.is_staff == False):
        return redirect(reverse("home"))
    return render(request,"staff/staff_view.html")

def staffZakupki(request):
    if(request.user.is_staff == False):
        return redirect(reverse("home"))
    prod = Products.objects.filter(count__lte = 3)
    return render(request,"staff/staff_zakupki.html",{"prod":prod})

def staffEditor(request):
    if(request.user.is_staff == False):
        return redirect(reverse("home"))

    prod = Products.objects.all()
    return render(request,"staff/staff_editor.html",{"prod":prod})

def staffEditorCompl(request,pk):

    if(request.user.is_staff == False):
        return redirect(reverse("home"))

    prod = Products.objects.get(id=pk)

    if(request.method == "POST"):
        name = request.POST.get("name")
        article = request.POST.get("article")
        price = request.POST.get("price")
        count = request.POST.get("count")
        print("all good")
        if(name != None):
            prod.name = name
            prod.save()
        if(article != None):
            prod.article = article
            prod.save()
        if(price != None):
            prod.price = price
            prod.save()
            print(price)
        if(count != None):
            prod.count = int(count)
            prod.save()
            print(count)

        return redirect(reverse("staff_editor"))


    return redirect(reverse("staff_editor"))