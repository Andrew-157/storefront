from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    # Sorts products by unit_price in ASC order and returns first object
    queryset = Product.objects.earliest('unit_price')
    # Sorts products by unit_price in DESC order and returns first object
    queryset = Product.objects.latest('unit_price')
    return render(request, 'hello.html', {'name': 'Andrew', 'products': list(queryset)})
