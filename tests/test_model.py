from django.test import TestCase
from django.contrib.auth import get_user_model

from kitchen.models import DishType, Dish


class ModelsTest(TestCase):
    def test_dish_type_str(self):
        dish_type_ = DishType.objects.create(
            name="test"
        )
        self.assertEquals(
            str(dish_type_), f"{dish_type_.name}"
        )

    def test_cook_str(self,):
        cook = get_user_model().objects.create_user(
            username="test",
            password="test12345",
            first_name="Test first",
            last_name="Test last"
        )
        self.assertEquals(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_str(self):
        dish_type_ = DishType.objects.create(
            name="test_nam",
        )
        dish = Dish.objects.create(
            name="test",
            description="test description",
            price=200.55,
            dish_type=dish_type_
        )
        self.assertEquals(str(dish), f"{dish.name}")

    def test_create_cook_with_experience(self):
        username = "test"
        password = "test12345"
        years_of_experience = 12
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )
        self.assertEquals(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEquals(cook.years_of_experience, years_of_experience)
