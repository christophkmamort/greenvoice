from django.views.generic import TemplateView
from django.shortcuts import render


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
