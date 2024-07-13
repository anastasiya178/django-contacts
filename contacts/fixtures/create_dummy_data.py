from contacts.fixtures.dummy_data import data
from contacts.models import Contact


c = {"first_name": "Leta", "last_name": "Coryndon", "email": "lcoryndon3@trellian.com"}
a = Contact(**c)
a.save()
