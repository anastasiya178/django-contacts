"""URLs for API application"""

from django.urls import path
from .views import ContactList, ContactDetail

app_name = "api"

urlpatterns = [
    path('contacts/', ContactList.as_view(), name="api_contacts_list"),
    path('contacts/<int:pk>', ContactDetail.as_view(), name="api_contact_detail"),
    path('delete/<int:pk>', ContactDetail.as_view(), name="api_contact_delete")
]