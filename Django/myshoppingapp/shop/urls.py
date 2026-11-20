from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.product_list, name="product_list"),
path("cart/add/<int:product_id>/", views.cart_add, name="cart_add"),
]
