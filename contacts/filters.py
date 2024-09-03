import django_filters
from contacts.models import Contact

class ContactFilter(django_filters.FilterSet):
    """ Search filter by last name for Contact list page """
    last_name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Contact
        fields = ['last_name']
