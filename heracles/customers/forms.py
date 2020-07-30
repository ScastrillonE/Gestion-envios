from django import forms

from .models import Customer
from departamentos.models import Departamento,Municipio


class CustomerForm(forms.ModelForm):
    TYPE_DOCUMENT = [
        ('Cedula', 'Cedula'),
        ('Cedula Extranjeria', 'Cedula Extranjeria'),
        ('Pasaporte', 'Pasaporte'),
        ('NIT', 'NIT'),
    ]
    class Meta:
        model = Customer
        fields = ['name', 'T_document', 'document', 'email', 'address', 'department', 'municipio', 'phone', 'cel']


    def __init__(self,*args,**kwargs):
        super(CustomerForm, self).__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

    # name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
    #     attrs={'class': 'form-control'}
    # ))
    # T_document = forms.ChoiceField(label='Tipo de documento', choices=TYPE_DOCUMENT,
    #                                required=True,  widget=forms.Select(attrs={'class':'form-control'}))
    #
    # document = forms.IntegerField(label='Numero de documento', required=True,
    #                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    #
    # email = forms.EmailField(label='Email', required=True,
    #                          widget=forms.EmailInput(attrs={'class': 'form-control'}))
    #
    # address = forms.CharField(label='Direccion', required=True, widget=forms.TextInput(
    #     attrs={'class': 'form-control'}
    # ))
    #
    # department = forms.ModelChoiceField(queryset=Departamento.objects.all(),
    #                                     widget=forms.Select(attrs={'class':'form-control'}))
    #
    # municipio = forms.ModelChoiceField(queryset=Municipio.objects.none(),
    #                                     widget=forms.Select(attrs={'class':'form-control'}))
    # phone = forms.IntegerField(label='Numero de telefono', required=False,
    #                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    #
    # cel = forms.IntegerField(label='Numero de celular', required=True,
    #                               widget=forms.TextInput(attrs={'class': 'form-control'}))

