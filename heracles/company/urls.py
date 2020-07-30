from django.urls import path
from .views import CompanyEdit

urlpatterns = [
    path('company/settings/<int:pk>/', CompanyEdit.as_view(), name='company_settings'),
]