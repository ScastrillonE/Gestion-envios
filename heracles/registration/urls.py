from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path, include

from .views import EmployeeCreateView

urlpatterns = [
    path('login', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('create', EmployeeCreateView.as_view(),name='employed_create')

]
