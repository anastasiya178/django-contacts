"""Unit tests for Contacts app"""

from django.http import response
from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.urls import reverse

from .models import Contact


# # creating a new contact
# class ContactModelTestCase(TestCase):
#     def setUp(self):
#         Contact.objects.create(name="Lion", email="lion@myemail.com")
#         Contact.objects.create(id="444", name="Lion", email="lion@myemail.com")
#
#     def test_get_absolute_url(self):
#         pass


# unauth user can't access the website
class GetHomePageTestCase(TestCase):

    def test_anonymous_cannot_see_page(self):
        """anonymous user can't access the website and gets redirected to Login page"""
        response = self.client.get(reverse("contacts:index"))
        self.assertRedirects(response, "/accounts/login/")

    def test_authenticated_user_can_see_page(self):
        """logged-in user can access the page"""
        user = User.objects.create_user("Katy", "katy_pass")
        self.client.force_login(user=user)
        response = self.client.get(reverse("contacts:index"))
        self.assertEqual(response.status_code, 200)

    def test_post_contact(self):
        """logged-in user with required permissions can create a new contact instance"""
        user = User.objects.create_user("Katy", "katy_pass")
        editor_group = Group.objects.create(name='Editor')
        editor_group.permissions.set([25, 28])
        editor_group.user_set.add(user)
        self.client.force_login(user=user)
        data = {"name": "Joe K", "email": "joe.s@gmail.com"}
        response = self.client.post(reverse("contacts:create_contact"), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("contacts:index"))



