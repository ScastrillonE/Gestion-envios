from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',  'email', 'password1', 'password2','groups']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Ingrese el nombre',
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Ingrese los apellidos',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Ingrese el correo',
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Ingrese la contraseña',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirme la contraseña',
        })
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Ingrese nombre de usuario',
        })

    def save(self, commit=True):
        form = super()
        try:
            if form.is_valid():
                print("LLEGUEE")
                u = form.save(commit=False)
                u.save()
                for g in self.cleaned_data['groups']:
                    u.groups.add(g)

        except Exception as e:
            print(e)

        return form
