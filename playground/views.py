from django.shortcuts import render
from django.db.models import Value, F, Count, Max, Sum
from store.models import Customer, Collection, Product


def say_hello(request):
    # Customers and their last order id
    queryset = Customer.objects.annotate(last_order_id=Max('order__id'))
    # Collections and count of their products
    queryset = Collection.objects.annotate(count_products=Count('product'))
    # Customers with more than 5 orders
    queryset = Customer.objects.annotate(
        count_orders=Count('order')).filter(count_orders__gt=5)
    # Customers and total amount they spent
    queryset = Customer.objects.annotate(
        total_spent=Sum(F('order__orderitem__unit_price') *
                        F('order__orderitem__quantity'))
    )
    # Top 5 best-selling products and their total sales
    queryset = Product.objects.annotate(
        total_sales=Sum(
            F('orderitem__unit_price') * F('orderitem__quantity')
        )
    ).order_by('-total_sales')[:5]
    return render(request, 'hello.html', {'name': 'Andrew', 'result': list(queryset)})
