from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    # sorts result by unit_price and returns first object
    queryset = Product.objects.earliest('unit_price')
    # sorts result by unit_price and returns last object
    queryset = Product.objects.latest('unit_price')
    return render(request, 'hello.html', {'name': 'Andrew', 'products': list(queryset)})
