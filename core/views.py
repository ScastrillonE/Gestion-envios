from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from company.models import CompanySettings
from customers.models import Customer
from shipments.models import Shipping
# Create your views here.


class BaseView(LoginRequiredMixin):
    login_url = 'login'

class IndexView(BaseView,TemplateView):
    template_name = 'core/index.html'

    def get(self, request, *args,**kwargs):
        if CompanySettings.objects.all().count() < 1:
            CompanySettings.create_company()
        return super().get(self, request, *args,**kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Customer.objects.all().count()
        context['enviados'] = Shipping.objects.filter(status="Enviado").count()
        context['pendientes'] = Shipping.objects.filter(status="Bodega").count()
        return context