"""Views for API app"""
import sys
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, exceptions
from contacts.models import Contact, Order, Product
from .serializers import ContactSerializer, OrderSerializer, ProductSerializer


# Create your API views here.

# permission classes
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
        if request.method == "PUT" and not request.user.has_perm('contacts.change_contact'):
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


# API views with permission classes included
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
    permission_classes = (UpdateContactPermission, DeleteContactPermission)  # doesn't make sense

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


class OrderList(APIView):
    """get all orders"""

    def get(self, request):
        api_orders = Order.objects.all()
        serializer = OrderSerializer(api_orders, many=True)
        return Response({"api_orders": serializer.data})


class OrderDetail(APIView):
    """get order detail"""
    def get_object(self, order_pk):
        try:
            return Order.objects.get(pk=order_pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, order_pk):
        order = self.get_object(order_pk)  #uses get_object function
        serializer = ContactSerializer(order)
        return Response(serializer.data)


class OrderListContact(generics.ListAPIView):
    """get all orders ordered by specified contact's ID"""
    serializer_class = OrderSerializer
    # model = serializer_class.Meta.model

    def get_queryset(self):
        """
        This view should return a list of all the orders for
        the contact as determined by the contact portion of the URL.
        """
        ordered_by = self.kwargs['pk'] #kwargs include pk (from url) and __len__
        # pk1 = self.kwargs['ordered_by']  # error as ordered_by not in kwargs
        return Order.objects.filter(ordered_by=ordered_by)


class OrderContactDetail(APIView):
        """This view should return order detail ordered by contact
        If it exists"""
        def get_object(self, order_pk):
            try:
                return Order.objects.get(pk=order_pk)
            except Order.DoesNotExist:
                raise Http404

        def get(self, request, order_pk, **kwargs):
            ordered_by = self.kwargs['pk']  # connect view with contact pk in URL
            if Order.objects.filter(ordered_by=ordered_by).exists():
                order = self.get_object(order_pk)  # uses get_object function
                serializer = OrderSerializer(order)
                return Response(serializer.data)
            else:
                raise Http404


class ProductList(APIView):
    pass


class ProductListContact(APIView):
    pass


class ProductDetail(APIView):
    pass


class ProductDetailContact(APIView):
    pass
