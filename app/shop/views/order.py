import json

from django.http import JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import render

from shop.models.order import Order, OrderItem
from shop.models.product import Product


class CartView(TemplateView):
    template_name = 'shop/cart.html'

    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, status=1)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}

        context = {
            'items':items,
            'order':order}
        return render(request, self.template_name, context)


class CheckoutView(TemplateView):
    template_name = 'shop/checkout.html'

    def get(self, request):
        addressIconStyle = 'opacity: 25%';
        paymentIconStyle = 'opacity: 25%';
        summaryIconStyle = 'opacity: 25%';

        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, status=1)
            items = order.orderitem_set.all()
        else:
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            items = []

        if 1 == 1:
            addressIconStyle = '';
        if 1 == 1:
            paymentIconStyle = '';
        if 1 == 1:
            summaryIconStyle = '';

        context = {
            'items':items,
            'order':order,
            'addressIconStyle':addressIconStyle,
            'paymentIconStyle':paymentIconStyle,
            'summaryIconStyle':summaryIconStyle,}
        return render(request, self.template_name, context)


class OrderView(TemplateView):
    template_name = 'shop/order.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class OrdersView(TemplateView):
    template_name = 'shop/profile-orders.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class RefundView(TemplateView):
    template_name = 'shop/refund.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


def updateCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, status=1)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
        message = 'added'
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        message = 'removed'

    orderItem.save()

    if orderItem.quantity <= 0 or action == 'delete':
        orderItem.delete()
        message = 'deleted'


    return JsonResponse(message, safe=False)


"""class UpdateCart(TemplateView):

    def get(self, request):
        return JsonResponse('Item was added', safe=False)"""
