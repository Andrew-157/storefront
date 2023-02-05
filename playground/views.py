from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem


def say_hello(request):
    ordered = OrderItem.objects.values_list('product_id').distinct()
    queryset = Product.objects.filter(id__in=ordered).order_by('title')
    return render(request, 'hello.html', {'name': 'Andrew', 'products': list(queryset)})
