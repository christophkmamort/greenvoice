from django.views.generic import TemplateView
from django.shortcuts import render

class IndexView(TemplateView):
    template_name = 'shop/index.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
