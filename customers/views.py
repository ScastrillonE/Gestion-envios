from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, \
    CreateView, DeleteView, UpdateView, TemplateView

from core.mixins import ValidateRequiredMixin
from core.views import BaseView
from .models import Customer
from .forms import CustomerForm
from departamentos.models import Municipio, Departamento


# Create your views here.

class ListarUsuarios(BaseView, ListView):
    model = Customer
    template_name = 'customers/list_customer.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data = []
            for i in Customer.objects.all():
                data.append(i.toJson())
            # print(data)
            return JsonResponse(data, safe=False)
        else:
            return render(request, self.template_name)


class CreateCustomer(BaseView, TemplateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/form_customer.html'

    def post(self, request, *args, **kwargs):
        data = {}
        if request.is_ajax():
            try:
                action = request.POST['action']
                print(action)
                if action == 'search_mun':
                    data = []
                    for i in Municipio.objects.filter(departamento_id=request.POST['id']):
                        data.append({'id': i.id, 'text': i.nombre})
                else:
                    print('Accion no contemplada')

            except Exception as e:
                print(e)
            return JsonResponse(data, safe=False)
        else:
            form = CustomerForm(request.POST)

            if form.is_valid():
                form.save()
                print("Guardado")

            return redirect(reverse_lazy('list_customer'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Usuario nuevo'
        context['title_button'] = 'Crear'
        context['form'] = self.form_class

        return context

    # def post(self,request,*args,**kwargs):
    #     if request.is_ajax():
    #         form = CustomerForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             print("Exito")
    #             data = {'mensaje':'registrado'}
    #         return JsonResponse(data)


class DeleteCustomer(ValidateRequiredMixin, DeleteView):
    permission_required = 'customers.delete_customer'
    model = Customer
    template_name = 'customers/delete.html'
    context_object_name = 'obj'
    url_redirect = reverse_lazy('list_customer')

    def delete(self, request, *args, **kwargs):
        self.object = self.model.objects.get(id=self.kwargs['pk'])
        self.object.delete = True
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)


class UpdateCustomer(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/form_customer.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('list_customer')

    def post(self, request, *args, **kwargs):
        data = {}
        if request.is_ajax():
            try:
                action = request.POST['action']
                print(action)
                if action == 'search_mun':
                    data = []
                    for i in Municipio.objects.filter(departamento_id=request.POST['id']):
                        data.append({'id': i.id, 'text': i.nombre})
                else:
                    print('Accion no contemplada')

            except Exception as e:
                print(e)
            return JsonResponse(data, safe=False)
        else:
            return super().post(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['title_button'] = 'Actualizar'
        return context
