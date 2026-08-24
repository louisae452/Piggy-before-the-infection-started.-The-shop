from django.test import TestCase
from .forms import RatingForm


class TestRatingForm(TestCase):
    """Tests RatingForm"""
    def test_form_is_valid(self):
        """Tests RatingForm is valid if all fields filled in correctly"""
        data = {
            'title': 'Not good',
            'comment': 'I did not like this item at all',
        }
        rating_form = RatingForm(data)
        self.assertTrue(rating_form.is_valid())

    def test_form_is_not_valid_no_title(self):
        """Tests RatingForm is not valid if title is missing"""
        data = {
            'title': '',
            'comment': 'I did not like this item at all',
        }
        rating_form = RatingForm(data)
        self.assertFalse(rating_form.is_valid())

    def test_form_is_not_valid_no_comment(self):
        """Tests RatingForm is not valid if comment is missing"""
        data = {
            'title': 'Not good',
            'comment': '',
        }
        rating_form = RatingForm(data)
        self.assertFalse(rating_form.is_valid())
