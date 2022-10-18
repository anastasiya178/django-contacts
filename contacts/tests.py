"""Unit tests for Contacts app"""
import unittest

from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.urls import reverse

from .models import Contact


class GetHomePageAnonymousTestCase(TestCase):
    @unittest.skip("In development")
    def test_anonymous_get_page(self):
        """Assert that anonymous user can't access the web page and gets redirected to Login page"""
        response = self.client.get(reverse("contacts:index"))
        self.assertRedirects(response, "/accounts/login/")


class GetHomePageAuthenticatedTestCase(TestCase):
    def setUp(self) -> None:
        """"Set up a user, log them in. Create a new contact"""
        self.user = User.objects.create_user("Katy", "katy_pass")
        self.client.force_login(user=self.user)

        self.contact = Contact(first_name="Harry", last_name="Jones", email="hatj@mail.com")
        self.contact.save()

    def test_authenticated_user_get_page(self):
        """Assert that authenticated user with no permissions assigned can access the web page"""
        response = self.client.get(reverse("contacts:index"))
        self.assertEqual(response.status_code, 200)


class GetHomePageAdminTestCase(TestCase):
    def setUp(self) -> None:
        """"Set up a user, log them in. Create a new contact"""
        self.user = User.objects.create_user("Katy", "katy_pass")
        editor_group = Group.objects.create(name='Admin')
        editor_group.permissions.set([25, 26, 27, 28])
        editor_group.user_set.add(self.user)
        self.client.force_login(user=self.user)

        self.contact = Contact(first_name="Harry", last_name="Jones", email="hatj@mail.com")
        self.contact.save()

    def test_admin_view_index_page(self):
        """Assert that authenticated Admin user can access the web page and gets redirected to Login page"""
        response = self.client.get(reverse("contacts:index"))
        self.assertEqual(response.status_code, 200)

    @unittest.skip("In development")
    def test_create_contact(self):
        """Assert that authenticated user with Editor permissions can create a new contact"""
        new_contact_data = {'first_name': 'Iris', 'last_name': 'Jones', 'email': 'irisj@mygmail.com'}
        response = self.client.post(reverse("contacts:create_contact"), new_contact_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("contacts:index"))

    def test_edit_contact(self):
        """Assert that authenticated user with Admin permissions can edit a contact
        TBD
        """
        pass

    def test_delete_contact(self):
        """Assert that authenticated user with Admin permissions can delete a contact instance"""
        url = reverse("contacts:delete_contact", args=[self.contact.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("contacts:index"))


class GetHomePageEditorTestCase(TestCase):
    def setUp(self) -> None:
        """"Set up a user, log them in. Create a new contact"""
        self.user = User.objects.create_user("Katy", "katy_pass")
        editor_group = Group.objects.create(name='Editor')
        editor_group.permissions.set([25, 28])
        editor_group.user_set.add(self.user)
        self.client.force_login(user=self.user)

        self.contact = Contact(first_name="Harry", last_name="Jones", email="hatj@mail.com")
        self.contact.save()

    def test_view_index_page(self):
        """Assert that authenticated Editor user can access the index page"""
        response = self.client.get(reverse("contacts:index"))
        self.assertEqual(response.status_code, 200)

    @unittest.skip("In development")
    def test_create_contact(self):
        """Assert that authenticated user with Editor permissions can create a new contact"""
        new_contact_data = {'first_name': 'Iris', 'last_name': 'Jones', 'email': 'irisj@mygmail.com'}
        response = self.client.post(reverse("contacts:create_contact"), new_contact_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("contacts:index"))

    def test_edit_contact(self):
        """Assert that authenticated user with Editor permissions can edit a new contact
        TBD
        """
        pass

    def test_delete_contact(self):
        """Assert that authenticated user with Editor permissions cannot delete a contact instance"""
        url = reverse("contacts:delete_contact", args=[self.contact.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 403)
