"""Views for API app"""

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, exceptions
from contacts.models import Contact
from .serializers import ContactSerializer


# Create your API views here.


class CreateContactPermission(permissions.BasePermission):
    """
     Create Contact Permission for users with 'contacts.add_contact' perm
     """
    def has_permission(self, request, view):
        if request.method == "POST" and not request.user.has_perm('contacts.add_contact'):
            raise exceptions.PermissionDenied("No permission to create a new contact")
        return True


class UpdateContactPermission(permissions.BasePermission):
    """
     Update Contact Permission for users with 'contacts.update_contact' perm
     """
    def has_permission(self, request, view):
        if request.method == "PUT" and not request.user.has_perm('contacts.update_contact'):
            raise exceptions.PermissionDenied("No permission to update a contact")
        return True


class DeleteContactPermission(permissions.BasePermission):
    """
     Delete Contact Permission for users with 'contacts.delete_contact' perm
     """
    def has_permission(self, request, view):
        if request.method == "DELETE" and not request.user.has_perm('contacts.delete_contact'):
            raise exceptions.PermissionDenied("No permission to delete a contact")
        return True


class ContactList(APIView):
    """
    List all contacts or create a new contact
    """
    permission_classes = (CreateContactPermission,)

    def get(self, request):
        api_contacts = Contact.objects.all()
        serializer = ContactSerializer(api_contacts, many=True)
        return Response({"api_contacts": serializer.data})

    def post(self, request):
        contact = request.data
        serializer = ContactSerializer(data=contact)
        if serializer.is_valid(raise_exception=True):
            contact_saved = serializer.save()
            return Response({"success": "Contact '{}' created successfully".format(contact_saved)})


class ContactDetail(APIView):
    """
    Retrieve, update or delete a contact instance.
    """
    permission_classes = (UpdateContactPermission, DeleteContactPermission) # doesn't make sense

    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = self.get_object(pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
