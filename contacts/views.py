"""Views for Contacts app"""

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from contacts.models import Contact

# Create your views here.


class ContactList(ListView):
    model = Contact


class ContactCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'contacts.add_contact'
    model = Contact
    fields = ('name', 'email')


class ContactDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'contacts.delete_contact'
    model = Contact
    success_url = reverse_lazy('contacts:index')
