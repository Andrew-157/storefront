from django.shortcuts import render
from store.models import Product


def say_hello(request):
    # inventory < 10 AND unit price < 20
    queryset = Product.objects.filter(
        inventory__lt=10).filter(unit_price__lt=20)
    return render(request, 'hello.html', {'name': 'Andrew', 'products': list(queryset)})
