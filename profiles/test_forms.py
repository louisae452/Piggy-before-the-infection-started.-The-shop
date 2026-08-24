from django.test import TestCase
from .forms import EmailForm, ProfileForm, UserForm


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
            'fistt_name': 'Johan',
            'last_name': '',
        }
        user_form = UserForm(data)
        self.assertFalse(user_form.is_valid())


class TestEmailForm(TestCase):
    """Tests EmailForm"""
    def test_form_is_valid(self):
        """Tests EmailForm is valid when email filled in correctly"""
        data = {
            'email': 'test@example.com',
        }
        email_form = EmailForm(data)
        self.assertTrue(email_form.is_valid())


class TestProfileForm(TestCase):
    """Tests ProfileForm"""
    def test_form_is_valid(self):
        """Tests ProfileForm is valid when all the required fields are filled
            in"""
        data = {
            'street_address1': '23 Mapple Road',
            'town': 'Lucella',
            'postcode': 'LU3 2PT',
        }
        profile_form = ProfileForm(data)
        self.assertTrue(profile_form.is_valid())

    def test_form_is_not_valid_no_street_address1(self):
        """Tests ProfileForm is not valid when street_address1 is missing"""
        data = {
                'street_address1': '',
                'town': 'Lucella',
                'postscode': 'LU3 2PT',
            }
        profile_form = ProfileForm(data)
        self.assertFalse(profile_form.is_valid())

    def test_form_is_not_valid_no_twon(self):
        """Tests ProfileForm is not valid when town is missing"""
        data = {
            'street_address1': '23 Mapple Road',
            'town': '',
            'postscode': 'LU3 2PT',
        }
        profile_form = ProfileForm(data)
        self.assertFalse(profile_form.is_valid())

    def test_form_is_not_valid_no_postcode(self):
        """Tests ProfileForm is not valid when postcode is missing"""
        data = {
            'street_address1': '23 Mapple Road',
            'town': 'Lucella',
            'postscode': '',
        }
        profile_form = ProfileForm(data)
        self.assertFalse(profile_form.is_valid())
