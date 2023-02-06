from django.shortcuts import render
from django.db import connection
from store.models import Order, OrderItem, Product, Customer, Collection


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Andrew'})
