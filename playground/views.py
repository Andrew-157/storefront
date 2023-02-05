from django.shortcuts import render
from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(last_update__year=2021)
    return render(request, 'hello.html', {'name': 'Andrew', 'products': list(queryset)})
