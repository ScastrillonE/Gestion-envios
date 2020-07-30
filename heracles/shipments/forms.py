from django import forms
from .models import Shipping,ShippingCompany

class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ['customer', 'c_Tdocument', 'c_document', 'c_address',
                  'c_department','c_municipio','c_phone', 'c_cel', 'c_email' ,'shipping_number',
                  'shipping_company', 'send_date', 'status','observations',
                  'weight','photo']

    def __init__(self, *args, **kwargs):
        super(ShippingForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

        self.fields['send_date'].widget.attrs.update({
            'input_formats':'%Y-%m-%d',
        })
        self.fields['observations'].widget.attrs.update({
            'rows':3,
        })
        self.fields['photo'].widget.attrs.update({
            'readonly':True,
            'hidden':True,
        })

class ShippingCompanyForm(forms.ModelForm):
    class Meta:
        model = ShippingCompany
        fields = ['name']

    def __init__(self,*args,**kwargs):
        super(ShippingCompanyForm, self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})

