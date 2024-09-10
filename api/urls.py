"""URLs for API application"""

from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views import ContactList, ContactDetail

app_name = "api"

schema_view = get_schema_view(
    openapi.Info(
        #  add your swagger doc title
        title="Contacts API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('contacts/', ContactList.as_view(), name="api_contacts_list"),
    path('contacts/<int:pk>', ContactDetail.as_view(), name="api_contact_detail"),
    path('delete/<int:pk>', ContactDetail.as_view(), name="api_contact_delete"),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
