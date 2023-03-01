from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from shop.models import *
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.

def cart_details(request,tot=0,count=0):
    ct = CartList.objects.get(cart_id=c_id(request))
    ct_items = CartItems.objects.filter(cart=ct,active=True)
    for i in ct_items:
        tot += (i.prodt.price*i.quan)
        count += i.quan

    return render(request, 'cart.html',{'ci':ct_items,'t':tot,'cn':count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id

def add_cart(request,product_id):
    prod= Products.objects.get(id=product_id)

    try:
        ct = CartList.objects.get(cart_id=c_id(request))
    except CartList.DoesNotExist:
        ct =CartList.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = CartItems.objects.get(cart=ct,prodt=prod)
        if c_items.quan < c_items.prodt.stock:
            c_items.quan += 1
        c_items.save()

    except (CartItems.DoesNotExist):
        c_items = CartItems.objects.create(cart=ct,prodt=prod,quan=1)
        c_items.save()
    return redirect("cartDetails")

def min_cart(request,product_id):
    ct=CartList.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(Products,id=product_id)
    c_items=CartItems.objects.get(cart=ct,prodt=prod)
    if c_items.quan>1:
        c_items.quan-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect("cartDetails")

def remove_cart(request,product_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(Products,id=product_id)
    c_items=CartItems.objects.get(cart=ct,prodt=prod)
    c_items.delete()
    return redirect("cartDetails")