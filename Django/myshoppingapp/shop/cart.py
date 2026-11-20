from decimal import Decimal

from .models import Product

CART_SESSION_KEY = "shopping_cart"


def get_cart(request):
    cart_data = request.session.get(CART_SESSION_KEY, {})
    product_ids = [int(product_id) for product_id in cart_data]

    products = Product.objects.filter(
        id__in=product_ids,
        is_available=True,
    )

    items = []
    total = Decimal("0.00")

    for product in products:
        quantity = min(
            int(cart_data.get(str(product.id), 0)),
            product.stock,
        )

        if quantity <= 0:
            continue

        line_total = product.price * quantity
        total += line_total

        items.append({
            "product": product,
            "quantity": quantity,
            "line_total": line_total,
        })

    return items, total


def get_cart_count(request):
    cart = request.session.get(CART_SESSION_KEY, {})
    return sum(int(quantity) for quantity in cart.values())