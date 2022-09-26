from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Product
from cart.cart import Cart


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
