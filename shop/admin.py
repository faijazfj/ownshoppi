from django.contrib import admin
from .models import *

# Register your models here.

class CategModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(categ,CategModel)


class ProdModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Products,ProdModel)

