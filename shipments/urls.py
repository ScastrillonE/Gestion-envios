from django.urls import path

from .views import (shipping, ListShipping, ShippingCompanyView,
deleteShipping, ShippingCompanyDelete,ShippingCompanyList,ShipppingCompanyEdit,
                    create_pdf)
from .reportes import reportes

urlpatterns = [
    path('shipping/list', ListShipping.as_view(), name="list_shipping"),
    path('shipping/<int:id_ship>/', shipping, name="edit_shipping"),
    path('shipping/create/', shipping, name="create_shipping"),
    path('shipping/delete/<int:pk>/',deleteShipping, name='delete_shipping'),
    # path ShippingCompany
    path('shipping/company/create/', ShippingCompanyView.as_view(),
         name='company_create'),
    path('shipping/company/delete/<int:pk>/',ShippingCompanyDelete.as_view(),
         name='company_delete'),
    path('shipping/company/list',ShippingCompanyList.as_view(),
         name='shippingCompany_list'),
    path('shipping/company/edit/<int:pk>/',ShipppingCompanyEdit.as_view(),
         name='shippingCompany_edit'),

    # Path reportes
    path('reporte/<str:f1>/<str:f2>/', reportes, name='reporte_rango'),
    
    #PDF
    path('create/pdf/<int:pk>/',create_pdf,name='create_pdf')
]
