from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


def get_cart_size(request):
    items = Cart(request).cart.items()
    quantity = 0
    for item in items:
        quantity += item[1]["quantity"]
    return quantity


@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    for key, value in cart.cart.copy().items():
        if value["quantity"] <= 0:
            product = Product.objects.get(id=value['product_id'])
            cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required()
def cart_detail(request):
    return render(request, 'mycart/cart_detail.html', context={'cart_size': get_cart_size(request)})
