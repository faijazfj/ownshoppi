from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    prod = Products.objects.all()

    return render(request,'index.html',{'pr':prod})