from django.shortcuts import render
from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    queryset = Customer.objects.filter(email__contains='.com')
    queryset_1 = Collection.objects.filter(featured_product__isnull=True)
    queryset_2 = Product.objects.filter(inventory__lt=10)
    queryset_3 = Order.objects.filter(customer__id=1)
    queryset_4 = OrderItem.objects.filter(product__collection__id=3)
    return render(request, 'hello.html', {'name': 'Andrew', 'products': list(queryset_4)})
