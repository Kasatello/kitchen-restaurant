from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from kitchen.models import DishType, Dish, Cook

DISH_TYPE_URL = reverse("kitchen:dish_type-list")
DISH_URL = reverse("kitchen:dish-list")
COOK_URL = reverse("kitchen:cook-list")


class PublicDishTypeTests(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)

        self.assertNotEqual(res.status_code, 302)


class PrivateDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_type(self):
        DishType.objects.create(name="Pasta")

        response = self.client.get(DISH_TYPE_URL)
        dish_types = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

    def test_search_dish_type_by_name(self):
        DishType.objects.create(name="Test Dish Type")
        searched_name = "Test"
        response = self.client.get(
            DISH_TYPE_URL,
            {"name": searched_name}
        )
        self.assertEqual(response.status_code, 200)
        dish_type_in_context = DishType.objects.filter(
            name__icontains=searched_name
        )
        self.assertQuerysetEqual(
            response.context["dish_type_list"], dish_type_in_context
        )


class PublicDishTests(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_URL)

        self.assertNotEqual(res.status_code, 302)


class PrivateDishTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password123",
            "21"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish(self):
        dish_type = DishType.objects.create(name="PASTA")
        Dish.objects.create(
            name="test",
            description="test description",
            price=14.88,
            dish_type=dish_type
        )

        response = self.client.get(DISH_URL)
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_search_dish_by_name(self):
        dish_type = DishType.objects.create(name="Pasta")
        Dish.objects.create(
            name="Karbonara",
            description="Test description",
            price=123.45,
            dish_type=dish_type)
        searched_name = "KAR"
        response = self.client.get(
            DISH_URL,
            {"name": searched_name}
        )
        self.assertEqual(response.status_code, 200)
        dish_in_context = Dish.objects.filter(name__icontains=searched_name)
        self.assertQuerysetEqual(response.context["dish_list"], dish_in_context)


class PublicCookTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(COOK_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="cook12345",
            years_of_experience=12
        )
        self.client.force_login(self.cook)

    def test_retrieve_cook(self):
        Cook.objects.create(username="test")
        response = self.client.get(COOK_URL)
        cooks = Cook.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks)
        )
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_search_cook_by_name(self):
        Cook.objects.create(username="test_cook")
        searched_username = "test"
        response = self.client.get(
            COOK_URL,
            {"username": searched_username}
        )
        self.assertEqual(response.status_code, 200)
        cook_in_context = Cook.objects.filter(
            username__icontains=searched_username
        )
        self.assertQuerysetEqual(
            response.context["cook_list"], cook_in_context, ordered=False
        )
