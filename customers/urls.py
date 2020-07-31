from django.urls import path
from .views import ListarUsuarios, CreateCustomer,\
    DeleteCustomer,UpdateCustomer

urlpatterns = [
    path('customer/list', ListarUsuarios.as_view(), name='list_customer'),
    path('customer/create', CreateCustomer.as_view(), name='create_customer'),
    path('customer/delete/<int:pk>/',DeleteCustomer.as_view(),name='delete_customer'),
    path('customer/update/<int:pk>/', UpdateCustomer.as_view(),name='update_customer'),

]
