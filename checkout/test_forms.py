
from django.test import TestCase
from .forms import OrderForm, UserForm


class TestUserForm(TestCase):
    """Tests UserForm form"""
    def test_form_is_valid(self):
        """Tests the form is valid when all fields are filled in correctly"""
        data = {
            'first_name': 'Johan',
            'last_name': 'Strauss',
        }
        user_form = UserForm(data)
        self.assertTrue(user_form.is_valid())

    def test_form_is_not_valid_first_name(self):
        """Tests the form is not valid if first_name is missing"""
        data = {
            'first_name': '',
            'last_name': 'Strauss',
        }
        user_form = UserForm(data)
        self.assertFalse(user_form.is_valid())

    def test_form_is_not_valid_last_name(self):
        """Tests the form is not valid if last_name is missing"""
        data = {
            'first_name': 'Johan',
            'last_name': '',
        }
        user_form = UserForm(data)
        self.assertFalse(user_form.is_valid())


class TestOrderForm(TestCase):
    """Tests OrderForm"""
    def test_order_form_is_valid(self):
        """Tests Order form is valid is all appropriate fields are filled in
            correctly"""
        data = {
            'email': 'test@example.com',
            'street_address1': '23 Mapple Road',
            'town': 'Lucella',
            'postcode': 'LU1 3PR'
        }
        order_form = OrderForm(data)
        self.assertTrue(order_form.is_valid())

    def test_order_form_is_not_valid_no_email(self):
        """Tests OrderForm is not valid if there is no email address"""
        data = {
            'email': '',
            'street_address1': '23 Mapple Road',
            'town': 'Lucella',
            'postcode': 'LU1 3PR',
        }
        order_form = OrderForm(data)
        self.assertFalse(order_form.is_valid())

    def test_order_form_is_not_valid_incorrect_email(self):
        """Tests OrderForm is not valid if email is incorrect"""
        data = {
                'email': 'example.com',
                'street_address1': '23 Mapple Road',
                'town': 'Lucella',
                'postcode': 'LU1 3PR',
            }
        order_form = OrderForm(data)
        self.assertFalse(order_form.is_valid())

    def test_order_form_is_not_valid_no_street_address1(self):
        """Tests OrderForm is not valid if street_address1 is missing"""
        data = {
            'email': 'test@example.com',
            'street_address1': '',
            'town': 'Lucella',
            'postcode': 'LU1 3PR',
        }
        order_form = OrderForm(data)
        self.assertFalse(order_form.is_valid())

    def test_order_form_is_not_valid_no_town(self):
        """Tests OrderForm is not valid if town is missing"""
        data = {
            'email': 'test@example.com',
            'street_address1': '23 Mapple Road',
            'town': '',
            'postcode': 'LU1 3PR',
        }
        order_form = OrderForm(data)
        self.assertFalse(order_form.is_valid())

    def test_order_form_is_not_valid_no_postcode(self):
        """Tests OrderForm is not valid if postcode is missing"""
        data = {
            'email': 'test@example.com',
            'street_address1': '23 Mapple Road',
            'town': 'Lucella',
            'postcode': '',
        }
        order_form = OrderForm(data)
        self.assertFalse(order_form.is_valid())
