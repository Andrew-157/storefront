from django.shortcuts import render
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product


def say_hello(request):
    result = Product.objects.aggregate(
        count=Count('id'), min_price=Min('unit_price'))
    result = Product.objects.filter(collection__id=6).aggregate(
        count=Count('id'), min_price=Min('unit_price'))
    return render(request, 'hello.html', {'name': 'Andrew', 'result': result})
