from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User, Group

from core.mixins import ValidateRequiredMixin
from .forms import SignUpForm


class EmployeeCreateView(ValidateRequiredMixin,CreateView):
    permission_required = 'registration.add_user'
    model = User
    form_class = SignUpForm
    template_name = 'registration/create.html'
    success_url = reverse_lazy('index')
    url_redirect = success_url
