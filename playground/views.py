from django.shortcuts import render
from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(collection__id=6)
    for product in queryset:
        print(product.collection.title)
    return render(request, 'hello.html', {'name': 'Andrew', 'products': list(queryset)})
