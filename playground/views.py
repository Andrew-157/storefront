from django.shortcuts import render
from django.db import transaction
from store.models import Order, OrderItem, Product, Customer, Collection


def say_hello(request):
    # this queryset is different from the previous
    # it doesn't have a lot of methods like filter, annotate etc.
    queryset = Product.objects.raw('SELECT * FROM store_product')
    return render(request, 'hello.html', {'name': 'Andrew', 'result': list(queryset)})
