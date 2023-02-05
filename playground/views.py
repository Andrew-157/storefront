from django.shortcuts import render
from django.db.models import Q
from store.models import Product


def say_hello(request):
    # inventory < 10 OR unit price < 20
    queryset = Product.objects.filter(
        Q(inventory__lt=10) | ~Q(unit_price__lt=20))
    return render(request, 'hello.html', {'name': 'Andrew', 'products': list(queryset)})
