from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView

from .models import CompanySettings
from .forms import CompanyForm
from core.mixins import ValidateRequiredMixin

# Create your views here.

class CompanyEdit(ValidateRequiredMixin,UpdateView):
    permission_required = 'company.change_companysettings'
    model = CompanySettings
    form_class = CompanyForm
    template_name = 'company/company_edit.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args,**kwargs):
        if self.model.objects.all().count() < 1:
            self.model.create_company()
        return super().get(self, request, *args,**kwargs)