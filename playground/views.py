from django.shortcuts import render
from django.db.models import Value, F, Func
from store.models import Customer


def say_hello(request):
    queryset = Customer.objects.annotate(
        full_name=Func(F('first_name'), Value(
            ' '), F('last_name'), function='CONCAT')
    )
    return render(request, 'hello.html', {'name': 'Andrew', 'result': list(queryset)})
