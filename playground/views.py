from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem


def say_hello(request):
    queryset = Product.objects.only('id', 'title')
    queryset = Product.objects.defer('description')
    return render(request, 'hello.html', {'name': 'Andrew', 'products': list(queryset)})
