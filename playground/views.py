from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    queryset = Product.objects.values('id', 'title', 'collection__title')
    return render(request, 'hello.html', {'name': 'Andrew', 'products': list(queryset)})
