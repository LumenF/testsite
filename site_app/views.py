from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView

from site_app.models import Category, Group, Product


class BaseView(TemplateView):

    def get(self, request, *args, **kwargs):
        categories = Group.objects.all()

        return render(request, 'html/base.html', {'categories': categories})


class DeviseMenu(DetailView):
    template_name = 'html/device.html'
    slug_url_kwarg = 'device'

    def get(self, request, *args, **kwargs):

        devices = Category.objects.filter(group=kwargs.get('device'))
        categories = Group.objects.all()
        return render(request, 'html/device.html', {'devices': devices,
                                                    'categories': categories})


class DeviceDetail(DetailView):
    template_name = 'html/detail.html'
    slug_url_kwarg = 'category'

    def get(self, request, *args, **kwargs):

        devices = Product.objects.filter(category=kwargs.get('category'))
        categories = Group.objects.all()
        return render(request, 'html/detail.html', {'devices': devices,
                                                    'categories': categories})


# .container {
#     display: grid;
#     grid-template-rows: 50px 50px;
# }