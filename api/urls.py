"""URLs for API application"""

from django.urls import path
from .views import ContactList, ContactDetail, OrderList, OrderListContact, OrderDetail, OrderContactDetail

app_name = "api"

urlpatterns = [
    path('contacts/', ContactList.as_view(), name="api_contacts_list"),
    path('contacts/<int:pk>/', ContactDetail.as_view(), name="api_contact_detail"),
    path('delete/<int:pk>/', ContactDetail.as_view(), name="api_contact_delete"),
    path('orders/', OrderList.as_view(), name="api_orders_list"),
    path('contacts/<int:pk>/orders/', OrderListContact.as_view(), name="api_orders_by_contact"),
    path('orders/<int:order_pk>/', OrderDetail.as_view(), name="api_order_detail"),
    path('contacts/<int:pk>/orders/<int:order_pk>/', OrderContactDetail.as_view(), name="api_order_detail_by_contact"),
]