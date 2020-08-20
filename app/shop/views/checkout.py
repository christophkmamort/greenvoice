from django.views.generic import TemplateView
from django.shortcuts import render

from shop.models.order import Order, OrderItem


class CheckoutView(TemplateView):
    template_name = 'shop/checkout.html'

    def get(self, request):
        checkoutStep = 1 # Checkout authentication
        checkoutAddressIcon = checkoutPaymentIcon = checkoutCheckIcon = 'opacity: 25%'

        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, status=1)
            items = order.orderitem_set.all()

            checkoutStep = 2
            checkoutAddressIcon = ''

        else:
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            items = []

        if 1 == 0: # Checkout payment
            checkoutStep = 3
            checkoutPaymentIcon = ''

        if 1 == 0: # Checkout confirm
            checkoutStep = 4
            checkoutCheckIcon = ''

        print(checkoutAddressIcon)


        context = {
            'checkoutAddressIcon':checkoutAddressIcon,
            'checkoutCheckIcon':checkoutCheckIcon,
            'checkoutPaymentIcon':checkoutPaymentIcon,
            'checkoutStep':checkoutStep,
            'items':items,
            'order':order,}
        return render(request, self.template_name, context)
