from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from unittest.mock import patch
from products.models import Product, Category, Group
from profiles.models import Profile


class TestCheckout(TestCase):
    """Tests checkout view"""
    def setUp(self):
        """Sets up url.
        Creates user and user profile
        Creates product
        Creates shopping bag
        Creates valid post data
        """
        self.client = Client()
        self.url = reverse('checkout:checkout')
        self.user = User.objects.create_user(
            username='Philip204',
            email='philip@example.com',
            password='passworf1',
            first_name='Philip',
            last_name='Marlow')
        self.profile, created = Profile.objects.get_or_create(user=self.user)
        self.profile.street_address1 = '34 Pine Road'
        self.profile.town = 'Lucella'
        self.profile.postcode = 'LU1 4PM'
        self.profile.save()
        category = Category.objects.create(name="Things", slug="3d-prints")
        group = Group.objects.create(
            name="small",
            category=category,
            slug="small")
        self.product = Product.objects.create(
            name="product",
            slug='product',
            price=10.00,
            group=group,
            code="TESTCODE")
        self.mock_bag = {

                         'items_total': 20.00,
                         'delivery': 4.99,
                         'total': 24.99,
                         'items': [
                             {'product': self.product,  'quantity': 2}
                            ]
                        }

    @patch('shopping_bag.context.bag_contents')
    def test_checkout_authenticated_user(self, mock_bag):
        """Tests checkout populates form data from logged in user"""
        mock_bag.return_value = self.mock_bag
        self.client.login(username='Philip204', password='password1')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_form', response.context)
        self.assertIn('address_form', response.context)

    def test_checkout_guest_user(self):
        """Tests checkout serves empty forms for unathenticated users"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class TestPaymentSuccess(TestCase):
    """Tests payment_success"""

    def test_payment_success_missing_info(self):
        """Tests mising session_id and missing order_id redirects with error"""
        url = reverse('checkout:payment_success')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products:allproducts'))
