from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Contact, Animal, Pet, Breed


# Register your models here.


# Contact Model
class ContactResource(resources.ModelResource):
    """
    TODO: what's the idea behind it?
    Class that integrates a django-import-export with Contact model.
    Describes how this resource can be imported or exported.
    django-import-export allows bulk importing and exporting contacts in Django admin.
    """
    class Meta:
        model = Contact


class ContactAdmin(ImportExportModelAdmin):
    """Admin integration is achieved by subclassing ImportExportModelAdmin or one of the available mixins"""
    resource_class = ContactResource


admin.site.register(Contact, ContactAdmin)
admin.site.register(Animal)
admin.site.register(Pet)
admin.site.register(Breed)