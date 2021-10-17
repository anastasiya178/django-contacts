"""REST API tests"""

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from contacts.models import Contact


class GetContactsTests(APITestCase):

    def test_get_contact_list(self):
        """
        ensure that authenticated user can access API contacts list for
        """
        user = User.objects.create_user("Katy", "katy_pass")
        self.client.force_login(user=user)
        url = reverse('api:api_contacts_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_contact_list_anonymous(self):
        """
        ensure that unauthenticated user can't access API contacts list,
        instead they get redirected to login page
        """
        url = reverse('api:api_contacts_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertRedirects(response, "/accounts/login/?next=/api/contacts/")

    def test_get_contact_detail(self):
        """ensure that authenticated user can access API contacts details
        """
        user = User.objects.create_user('Katy', "katy_pass")
        self.client.force_login(user=user)
        new_contact = Contact(name="Sally G", email="sallys@mail.com")
        new_contact.save()
        pk = new_contact.pk
        url = reverse('api:api_contact_detail', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.get().name, 'Sally G')

    def test_get_contact_detail_anonymous(self):
        """
        ensure that unauthenticated user can't access API contacts details,
        instead they get redirected to login page
        """
        new_contact = Contact(name="Sally G", email="sallys@mail.com")
        new_contact.save()
        pk = new_contact.pk
        url = reverse('api:api_contact_detail', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertRedirects(response, "/accounts/login/?next=/api/contacts/256")


class CRUDContactTests(APITestCase):
    def test_create_contact(self):
        """
        Ensure we can create a new contact object.
        """
        user = User.objects.create_user("Katy", "katy_pass")
        self.client.force_login(user=user)
        url = reverse('api:api_contacts_list')
        data = {'name': 'Iris', 'email': 'iris@mygmail.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.get().name, 'Iris')

    def test_update_contact(self):
        """
        Ensure we can update an existing contact object.
        """
        pass

    def test_delete_contact(self):
        """
        Ensure we can delete an existing contact object.
        """
        pass




