from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import DishType, Cook, Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "dish_type"]
    list_filter = ["dish_type"]
    search_fields = ["name"]


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)


admin.site.register(DishType)
