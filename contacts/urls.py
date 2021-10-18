"""URLs for Contacts app"""

from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path("", views.ContactList.as_view(), name="index"),
    path('create_contact/', views.ContactCreateView.as_view(), name='create_contact'),
    path('delete/<int:pk>/', views.ContactDeleteView.as_view(), name="delete_contact"),
    ]