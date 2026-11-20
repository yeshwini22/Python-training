from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Product


def product_list(request):
    products = Product.objects.filter(is_available=True, stock__gt=0)
    return render(request, "shop/product_list.html", {"products": products})


@require_POST
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_available=True)
    cart = request.session.get("shopping_cart", {})
    key = str(product.id)
    cart[key] = cart.get(key, 0) + 1
    request.session["shopping_cart"] = cart
    return redirect("shop:product_list")
def cart_detail(request):
    items, total = get_cart(request)
    return render(request, "shop/cart_detail.html", {
        "items": items,
        "total": total,
    })