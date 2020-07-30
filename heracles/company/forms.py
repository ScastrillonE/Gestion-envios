from django import forms

from .models import CompanySettings


class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanySettings
        fields = ['name_company', 'address', 'email', 'phone_number', 'cel', 'logo']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == 'logo':
                self.fields['logo'].widget.attrs.update({'class': 'mt-3'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
