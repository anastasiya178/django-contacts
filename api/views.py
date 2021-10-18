"""Views for API app"""

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from contacts.models import Contact
from .serializers import ContactSerializer


# Create your API views here.


class ContactList(APIView):
    """
    List all contacts or create a new contact
    """

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
    Retrieve, update or delete a snippet instance.
    """
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