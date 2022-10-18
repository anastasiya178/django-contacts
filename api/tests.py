"""REST API tests
"""
import unittest

from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from contacts.models import Contact


class RegistrationTest(APITestCase):
    """N/a since there is no opportunity to register on the website yet"""
    pass

class GetContactsTests(APITestCase):

    def setUp(self) -> None:
        """ Set up a user and log them in """
        user = User.objects.create_user("New_user", "pass123")
        self.client.force_login(user=user)


    def test_get_contact_list(self):
        """ Ensure that authenticated user can access API contacts list"""
        url = reverse('api:api_contacts_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_contact_detail(self):
        """ Ensure that authenticated user can access API contacts details"""
        new_contact = Contact(first_name="Christian", last_name="Jimene", email="sallysal@mail.com")
        new_contact.save()
        url = reverse('api:api_contact_detail', args=[new_contact.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.get().first_name, 'Christian')
        self.assertEqual(Contact.objects.get().last_name, 'Jimene')


class GetContactsAnonymousTests(APITestCase):

    @unittest.skip("auth restriction to view is not yet implemented")
    def test_get_contact_list_anonymous(self):
        """
        Ensure unauthenticated user can't access API contacts list,
        instead they get redirected to login page
        """
        url = reverse('api:api_contacts_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertRedirects(response, "/accounts/login/?next=/api/contacts/")

    @unittest.skip("auth restriction to view is not yet implemented")
    def test_get_contact_detail_anonymous(self):
        """
        Ensure unauthenticated user can't access API contacts details,
        instead they get redirected to login page
        """
        new_contact = Contact(first_name="Walker", last_name="Galloway", email="walker.galloway@mail.com")
        new_contact.save()
        url = reverse('api:api_contact_detail', args=[new_contact.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)


class CRUDAdminContactTests(APITestCase):

    def setUp(self) -> None:
        """ Create a new user with Admin permissions and log them in. Create a new contact and save it """
        self.user = User.objects.create_user("New_user", "pass123")
        self.editor_group = Group.objects.create(name='Admin')
        self.editor_group.permissions.set([25, 26, 27, 28])
        self.editor_group.user_set.add(self.user)
        self.client.force_login(user=self.user)
        self.contact = Contact(first_name="Harry", last_name="Jones", email="hatj@smail.com")
        self.contact.save()

    @unittest.skip("In development")
    def test_create_contact(self):
        """ Ensure Admin user can create a new contact """
        url = reverse('api:api_contacts_list')
        new_contact_data = {'first_name': 'Iris', 'last_name': 'Jones', 'email': 'irisj@mygmail.com'}
        response = self.client.post(url, new_contact_data, format='json')
        # need to add pk
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.get().first_name, 'Iris')

    def test_update_contact(self):
        """ Ensure Admin can update existing contact """
        url = reverse('api:api_contact_detail', args=[self.contact.pk])
        data = {'first_name': 'Iris'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.get(pk=self.contact.pk).first_name, 'Iris')

    def test_delete_contact(self):
        """ Ensure Admin user can delete an existing contact """
        url = reverse('api:api_contact_delete', args=[self.contact.pk])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CRUDEditorContactTests(APITestCase):

    def setUp(self) -> None:
        """ Create a new user with Editor permissions and log them in.
        Create a new contact and save it .
        Editor can view and delete the contacts.
        """
        self.user = User.objects.create_user("New_user", "pass123")

        self.editor_group = Group.objects.create(name='Editor')
        self.editor_group.permissions.set([25, 26])
        self.editor_group.user_set.add(self.user)

        self.client.force_login(user=self.user)

        self.contact = Contact(first_name="Harry", last_name="Jones", email="hatj@smail.com")
        self.contact.save()

    def test_create_contact(self):
        """ Ensure a new contact object can be created."""
        url = reverse('api:api_contacts_list')
        new_contact_data = {'first_name': 'Iris', 'last_name': 'Jones', 'email': 'irisj@mygmail.com'}
        response = self.client.post(url, new_contact_data, format='json') # doesn't work, error
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_contact(self):
        """ Ensure an existing contact object can be updated by Editor.
        """
        url = reverse('api:api_contact_detail', args=[self.contact.pk])
        data = {'first_name': 'Iris'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.contact.first_name, 'Iris') # doesn't work

    def test_delete_contact(self):
        """ Ensure existing contact object cannot be removed by Editor """
        url = reverse('api:api_contact_delete', args=[self.contact.pk])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)