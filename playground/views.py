from django.shortcuts import render
from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(unit_price__gt=20)
    return render(request, 'hello.html', {'name': 'Andrew', 'products': list(queryset)})
