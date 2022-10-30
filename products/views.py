from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Product
from cart.cart import Cart
from users.models import User


# Create your views here.
class BaseView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'all_products_list'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        items = Cart(self.request).cart.items()
        quantity = 0
        for item in items:
            quantity += item[1]["quantity"]
        context_data['cart_size'] = quantity
        return context_data


class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Product.objects.all()


def add_to_favourite(request, user_id, product_id):
    user = User.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    user.favourite_products.add(product)
    return redirect("products:base")


def favourite_products_page(request, user_id):
    template = 'products/favourite.html'
    favourite_products = Product.objects.select_related().get(id=user_id)
    print(favourite_products)
    return render(request, template, {'favourite': favourite_products})
