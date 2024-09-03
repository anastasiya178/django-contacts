"""Views for Contacts app"""

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from contacts.filters import ContactFilter
from contacts.models import Contact


# Create your views here.


class ContactList(ListView):
    model = Contact

    def get_context_data(self, **kwargs):
        """
        Extend or overwrite ContactList view context.
        Add filter.
        Overwrite page_obj for pagination.
        """
        # call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        contact_filter = ContactFilter(self.request.GET, queryset=Contact.objects.all())
        context['filter'] = contact_filter

        # overwrite pagination to include
        paginator = Paginator(contact_filter.qs, 20)  # Show 25 contacts per page.
        page_number = self.request.GET.get("page")
        page_obj_filtered = paginator.get_page(page_number)
        context['page_obj'] = page_obj_filtered
        return context


class ContactCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "contacts.add_contact"
    model = Contact
    fields = ("first_name", "last_name", "email")


class ContactDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "contacts.delete_contact"
    model = Contact
    success_url = reverse_lazy("contacts:index")

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
