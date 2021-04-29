from django.contrib.auth import get_user_model, authenticate, logout
from django.contrib.auth.models import User
from django.test.client import RequestFactory

from django.test import TestCase, Client


class SigninTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def test_correct_login(self):
        # request = self.factory.get('/account/')
        user = authenticate(username='test', password='12test12')
        self.assertTrue(True, user.is_authenticated)

    def test_correct_logout(self):
        user = authenticate(username='test', password='12test12')
        response = self.client.get('/account/')
        request = response.wsgi_request
        logout(request)
        self.assertFalse(False, user.is_authenticated)
