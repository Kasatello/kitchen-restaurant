from django.test import TestCase

from kitchen.forms import CookCreationForm, CookUpdateForm, DishForm


class FormsTests(TestCase):
    def test_cook_form_with_experience_first_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user12345",
            "password2": "user12345",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 12
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_dish_form_invalid(self):
        form_data = {
            'name': '',
            'description': 'This is a test dish.',
            'price': 'invalid_price',
            'dish_type': 1,
            'cooks': [1, 2],
        }
        form = DishForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_cook_update_form_if_valid(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'years_of_experience': 40,
        }
        form = CookUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())
