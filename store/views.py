from django.shortcuts import render

from django.shortcuts import render

from .models import *

from  django.http import JsonResponse

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer  # one to one relationship implement
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)  # order created or get order if exist
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer #one to one relationship implement
        order, created = Order.objects.get_or_create(customer = customer, complete=False) #order created or get order if exist
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order= {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    context = {'items':items,'order':order,'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer #one to one relationship implement
        order, created = Order.objects.get_or_create(customer = customer, complete=False) #order created or get order if exist
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order= {'get_cart_total':0, 'get_cart_items':0}
        cartItems =order['get_cart_items']
    context = {'items':items,'order':order,'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    return JsonResponse("Item was added", self=False)