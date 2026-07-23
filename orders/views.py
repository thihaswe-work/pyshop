from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Cart, CartItem, Order


def _get_cart(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.save()
        cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart


def cart_detail(request):
    cart = _get_cart(request)
    return render(request, "orders/cart.html", {"cart": cart})


def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = _get_cart(request)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f"{product.name} added to cart.")
    return redirect(request.META.get("HTTP_REFERER", "products:list"))


def cart_remove(request, product_id):
    cart = _get_cart(request)
    CartItem.objects.filter(cart=cart, product_id=product_id).delete()
    messages.success(request, "Item removed from cart.")
    return redirect("cart:detail")


def cart_update(request, product_id):
    cart = _get_cart(request)
    item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    qty = request.POST.get("quantity", 1)
    try:
        qty = int(qty)
        if qty > 0:
            item.quantity = qty
            item.save()
        else:
            item.delete()
    except ValueError:
        pass
    return redirect("cart:detail")


@login_required
def checkout(request):
    cart = _get_cart(request)
    if cart.total_items() == 0:
        messages.warning(request, "Your cart is empty.")
        return redirect("cart:detail")

    if request.method == "POST":
        order = Order.objects.create(
            user=request.user,
            full_name=request.POST["full_name"],
            email=request.POST["email"],
            address=request.POST["address"],
            phone=request.POST["phone"],
            notes=request.POST.get("notes", ""),
            total=cart.total_price(),
        )
        cart.items.all().delete()
        messages.success(request, "Order placed successfully!")
        return redirect("orders:order_detail", pk=order.id)

    return render(request, "orders/checkout.html", {"cart": cart})


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, "orders/order_detail.html", {"order": order})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "orders/order_history.html", {"orders": orders})
