from os import remove
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required, \
    permission_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DeleteView, CreateView, \
    ListView, UpdateView


from core.mixins import ValidateRequiredMixin
from .models import Shipping, ShippingCompany
from .forms import ShippingForm, ShippingCompanyForm
from .utils import *


from customers.models import Customer
from company.models import CompanySettings

from departamentos.models import Municipio


class ShippingCompanyView(LoginRequiredMixin, CreateView):
    model = ShippingCompany
    form_class = ShippingCompanyForm
    template_name = 'shipments/shipping_company_form.html'
    success_url = reverse_lazy('company_create')


class ShippingCompanyDelete(ValidateRequiredMixin, DeleteView):
    permission_required = 'shipments.delete_shippingcompany'
    model = ShippingCompany
    template_name = 'shipments/delete.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('shippingCompany_list')
    url_redirect = success_url

    def delete(self, request, *args, **kwargs):
        self.object = self.model.objects.get(id=self.kwargs['pk'])
        self.object.delete = True
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)


class ShippingCompanyList(LoginRequiredMixin, ListView):
    model = ShippingCompany
    template_name = 'shipments/shippingCompany_list.html'
    context_object_name = 'obj'


class ShipppingCompanyEdit(LoginRequiredMixin, UpdateView):
    model = ShippingCompany
    template_name = 'shipments/shipping_company_form.html'
    form_class = ShippingCompanyForm
    success_url = reverse_lazy('shippingCompany_list')


@csrf_exempt
@login_required(login_url=reverse_lazy('login'))
def shipping(request, id_ship=None):
    template_name = 'shipments/shipping_form.html'
    form = ShippingForm()

    data = []

    if request.method == "GET":
        form = form
        shipping = Shipping.objects.filter(id=id_ship).first()

        if shipping:
            datos_form = {
                'customer': shipping.customer,
                'c_Tdocument': shipping.c_Tdocument,
                'c_document': shipping.c_document,
                'c_address': shipping.c_address,
                'c_department': shipping.c_department,
                'c_municipio': shipping.c_municipio,
                'c_phone': shipping.c_phone,
                'c_cel': shipping.c_cel,
                'c_email': shipping.c_email,
                'shipping_company': shipping.shipping_company,
                'send_date': shipping.send_date,
                'status': shipping.status,
                'photo': shipping.photo,
                'shipping_number': shipping.shipping_number,
                'observations': shipping.observations,
                'weight': shipping.weight,
            }
            form_data = ShippingForm(datos_form)
            context = {'form': form_data, 'action': 'edit', 'id_ship': id_ship}
        else:
            context = {'form': form}

        return render(request, template_name, context)

    if request.method == "POST":
        # customer = request.POST.get("customer")
        # Tdocument = request.POST.get("c_Tdocument")
        # document = request.POST.get("c_document")
        # address = request.POST.get("c_address")
        # phone = request.POST.get("c_phone")
        # cel = request.POST.get("cel")
        # company = request.POST.get("shipping_company")
        # photo = request.POST.get("photo")

        if request.is_ajax():
            action = request.POST['action']
            print(action)
            if action == "search_data_customer":
                id = request.POST['id']

                for i in Customer.objects.filter(id=id):
                    data.append(i.toJson())

            elif action == "create_shipping":
                data = {}
                form = ShippingForm(request.POST)
                print(form.errors)
                estado_envio = request.POST['status']
                name = get_name(request.POST['customer'])
                email = request.POST['c_email']
                number = request.POST['shipping_number']
                send_date = request.POST['send_date']
                shipping_company = request.POST['shipping_company']
                shipping_company = ShippingCompany.objects.get(id=shipping_company)

                if form.is_valid():
                    form.save()
                    data['success'] = 'Guardado correctamente'
                    try:
                        if estado_envio == 'Enviado':
                            send_email(name, email, number, shipping_company.name, send_date)
                            print('Enviado')

                        data['success'] = 'Guardado correctamente'
                    except Exception as e:
                        data['error'] = str(e)


            elif action == "edit_shipping":
                data = {}
                shipping = Shipping.objects.filter(id=id_ship).first()
                form = ShippingForm(request.POST, instance=shipping)
                estado_envio = request.POST['status']
                name = get_name(request.POST['customer'])
                email = request.POST['c_email']
                number = request.POST['shipping_number']
                send_date = request.POST['send_date']
                shipping_company = request.POST['shipping_company']
                shipping_company = ShippingCompany.objects.get(id=shipping_company)

                if form.is_valid():
                    form.save()
                    try:
                        if estado_envio == 'Enviado':
                            send_email(name, email, number, shipping_company.name, send_date)
                            print('Enviado')

                        data['success'] = 'Guardado correctamente'
                    except Exception as e:
                        data['error'] = str(e)
                else:
                    data['error'] = 'Error al guardar {}'.format(form.errors)
            return JsonResponse(data, safe=False)

        # else:
        #     shipping = Shipping.objects.filter(id=id_ship).first()
        #
        #     if shipping:
        #         shipping.customer = Customer.objects.get(id=customer)
        #         shipping.c_Tdocument = Tdocument
        #         shipping.c_document = document
        #         shipping.c_address = address
        #         shipping.c_phone = phone
        #         shipping.c_cel = cel
        #         shipping.shipping_company = ShippingCompany.objects.get(id=company)
        #         shipping.photo = photo
        #         shipping.save()

        return JsonResponse(data, safe=False)


# class CreateShipping(CreateView):
#     model = Shipping
#     form_class = ShippingForm
#
#     def post(self,request,*args, **kwargs):
#         if request.is_ajax():
#             form = self.get_form()
#             print(form)
#             data = 'success'
#             return JsonResponse(data)

class ListShipping(LoginRequiredMixin, ListView):
    model = Shipping
    template_name = 'shipments/list_shipping.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data = []
            for i in Shipping.objects.all():
                data.append(i.toJson())
                # print(data)
            return JsonResponse(data, safe=False)
        else:
            return render(request, self.template_name)


class DeleteShipping(ValidateRequiredMixin, DeleteView):
    permission_required = 'shipments.delete_shipping'
    model = Shipping
    template_name = 'shipments/delete.html'
    context_object_name = 'obj'
    url_redirect = reverse_lazy('list_shipping')

    def delete(self, request, *args, **kwargs):
        self.object = self.model.objects.get(id=self.kwargs['pk'])
        self.object.delete = True
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)


def create_pdf(request, pk):
    template_name ='shipments/pdf.html'
    shipping = Shipping.objects.get(id=pk)
    company = CompanySettings.objects.get(id=1)

    codigo = generate_codebar(shipping.consecutivo)
    data = {
        'code': codigo,
        'shipping': shipping,
        'company': company,
    }
    return render_to_pdf(template_name, data)
