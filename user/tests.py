# user/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class UserRolesTest(TestCase):
    def setUp(self):
        self.customer = get_user_model().objects.create_user(
            username='customer_test',
            email='customer_test@example.com',
            password='testpassword',
            role='customer'
        )

        self.restaurant_owner = get_user_model().objects.create_user(
            username='owner_test',
            email='owner_test@example.com',
            password='testpassword',
            role='restaurant_owner'
        )

    def test_customer_can_access_customer_view(self):
        self.client.login(username='customer_test', password='testpassword')
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User Profile')

