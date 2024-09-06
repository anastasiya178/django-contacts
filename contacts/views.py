"""Views for Contacts app"""

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from contacts.filters import ContactFilter, PetFilter
from contacts.models import Contact, Pet


# Create your views here.
class FilteredListViewMixin:
    """ A mixin that adds a filter to ListView"""
    filter_class = None
    paginate_by = 10

    def get_filter(self):
        return self.filter_class(self.request.GET, queryset=self.model.objects.all())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Apply filtering
        object_filter = self.get_filter()
        context['filter'] = object_filter

        # Apply pagination
        paginator = Paginator(object_filter.qs, self.paginate_by)
        page_number = self.request.GET.get("page")
        page_obj_filtered = paginator.get_page(page_number)
        context['page_obj'] = page_obj_filtered

        return context


class ContactList(FilteredListViewMixin, ListView):
    model = Contact
    filter_class = ContactFilter


class ContactCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "contacts.add_contact"
    model = Contact
    fields = ("first_name", "last_name", "email")


class ContactDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "contacts.delete_contact"
    model = Contact
    success_url = reverse_lazy("contacts:index")


# Pets
# class PetList(FilteredListView):
class PetList(FilteredListViewMixin, ListView):
    model = Pet
    filter_class = PetFilter
    # if you specify paginate_by here, it will overwright the value in FilteredListView
    # paginate_by = 5

    # filter_fields = ["name"]

# Example of function-based view
# def current_datetime(request):
#     now = datetime.datetime.now()
#     curr_date = "It is now %s" % now
#     contact_list = Contact.objects.all()
#     template = loader.get_template("contacts/contacts_list_v2.html")
#     f = ContactFilter(request.GET, queryset=Contact.objects.all())
#     paginate_by = 10
#
#     context = {
#         "curr_date": curr_date,
#         "filter": f,
#         "contact_list": contact_list
#     }
#     return HttpResponse(template.render(context, request))
