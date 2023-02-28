from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.


def index(request,c_slug=None):
    c_page = None
    prodt = None
    if c_slug!=None:
        c_page = get_object_or_404(categ,slug=c_slug)
        prodt = Products.objects.filter(category=c_page,available=True)
    else:
        prodt = Products.objects.all().filter(available=True)
    cat = categ.objects.all()

    return render(request,'index.html',{'pr':prodt,'ct':cat})

def prodDetails(request,c_slug,product_slug):
    try:
        prod=Products.objects.get(category__slug=c_slug,slug=product_slug)

    except Exception as e:
        raise e
    return render(request,'item.html',{'pr':prod})

def searching(request):
    query=None
    prod=None

    if 'q' in request.GET:
        query =request.GET.get('q')
        prod = Products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))

    return render(request,'search.html',{'pr':prod,'q':query})


