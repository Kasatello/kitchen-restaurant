from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Cook, Dish, DishType


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )


class CookUpdateForm(forms.ModelForm):

    class Meta:
        model = Cook
        fields = ["first_name", "last_name", "years_of_experience"]

    def clean_years_of_experience(self):
        return validate_years_of_experience(
            self.cleaned_data["years_of_experience"]
        )


def validate_years_of_experience(
    years_of_experience,
):
    if not isinstance(years_of_experience, int) or years_of_experience < 0:
        raise ValidationError(
            "Years of experience must be a positive integer."
        )

    if not 0 <= years_of_experience <= 40:
        raise ValidationError(
            "Years of experience must be between 0 and 40."
        )

    return years_of_experience


class CookSearchForm(forms.ModelForm):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username..."})
    )

    class Meta:
        model = Cook
        fields = ["username"]


class DishSearchForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )

    class Meta:
        model = Dish
        fields = ["name"]


class DishTypeSearchForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )

    class Meta:
        model = DishType
        fields = ["name"]
