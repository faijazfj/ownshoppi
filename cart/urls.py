from django.urls import path
from . import views

urlpatterns = [
    path('cartDetails',views.cart_details,name='cartDetails'),
    path('add/<int:product_id>/',views.add_cart,name='add'),
    path('decrement/<int:product_id>/',views.min_cart,name='decrement'),
    path('remove/<int:product_id>/',views.remove_cart,name='remove')
]