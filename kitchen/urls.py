from django.urls import path

from kitchen.views import (CookCreateView, CookDeleteView, CookDetailView,
                           CookListView, CookUpdateView, DishCreateView,
                           DishDeleteView, DishDetailView, DishListByTypeView,
                           DishListView, DishTypeCreateView,
                           DishTypeDeleteView, DishTypeListView,
                           DishTypeUpdateView, DishUpdateView,
                           PermissionDeniedView, index)


class DriverCreateView:
    pass


urlpatterns = [
    path("", index, name="index"),
    path(
        "dishtype/",
        DishTypeListView.as_view(),
        name="dish_type-list"
    ),
    path(
        "dishtype/create/",
        DishTypeCreateView.as_view(),
        name="dish_type-create",
    ),
    path(
        "dishtype/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish_type-update",
    ),
    path(
        "dishtype/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish_type-delete",
    ),
    path(
        "dish/",
        DishListView.as_view(),
        name="dish-list"
    ),
    path("dish/<int:pk>/",
         DishDetailView.as_view(),
         name="dish-detail"
         ),
    path("dish/create/",
         DishCreateView.as_view(),
         name="dish-create"
         ),
    path("dish/<int:pk>/update/",
         DishUpdateView.as_view(),
         name="dish-update"
         ),
    path("dish/<int:pk>/delete/",
         DishDeleteView.as_view(),
         name="dish-delete"
         ),
    path(
        "dish-type/<int:pk>/",
        DishListByTypeView.as_view(),
        name="dish-list-by-type"
    ),
    path(
        "cook/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cook/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "cook/create/",
        CookCreateView.as_view(),
        name="cook-create"
    ),
    path(
        "cook/<int:pk>/update",
        CookUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "cook/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),
    path(
        "permission-denied/",
        PermissionDeniedView.as_view(),
        name="permission-denied")
]

app_name = "kitchen"
