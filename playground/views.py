from django.shortcuts import render
from django.db import connection
from store.models import Order, OrderItem, Product, Customer, Collection


def say_hello(request):
    with connection.cursor() as cursor:
        cursor.execute('')
        cursor.callproc()  # this executes stored procedures
    return render(request, 'hello.html', {'name': 'Andrew', 'result': list(queryset)})
