from django.contrib.auth import login
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import (CookCreationForm, CookSearchForm, CookUpdateForm,
                           DishForm, DishSearchForm, DishTypeSearchForm)
from kitchen.models import Cook, Dish, DishType


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_cooks": Cook.objects.count(),
        "num_dish_type": DishType.objects.count(),
        "num_dishes": Dish.objects.count()
    }
    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")

        context["search_form"] = DishTypeSearchForm(initial={
            "name": name
        })
        return context

    def get_queryset(self):
        form = DishTypeSearchForm(self.request.GET)

        if form.is_valid():
            return DishType.objects.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return DishType.objects.all()


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish_type-list")


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.all().select_related("dish_type")
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")

        context["search_form"] = DishSearchForm(initial={
            "name": name
        })
        return context

    def get_queryset(self):
        form = DishSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return Dish.objects.all()


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username")

        context["search_form"] = CookSearchForm(initial={
            "username": username
        })
        return context

    def get_queryset(self):
        form = CookSearchForm(self.request.GET)

        if form.is_valid():
            return self.model.objects.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return Cook.objects.all()


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen:cook-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CookUpdateView(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     generic.UpdateView):
    permission_required = "kitchen.change_cook"
    model = Cook
    form_class = CookUpdateForm
    template_name = "kitchen/cook_form.html"
    success_url = reverse_lazy("kitchen:cook-list")

    def test_func(self):
        return (self.request.user == self.get_object()
                or self.request.user.is_superuser)

    def handle_no_permission(self):
        context = {
            'action': 'update',
        }
        if self.request.user == self.get_object():
            return super().handle_no_permission()
        else:
            return render(
                self.request, "kitchen/permission_denied.html", context
            )


class CookDeleteView(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     generic.DeleteView):
    permission_required = "kitchen.delete_cook"
    model = Cook
    template_name = "kitchen/cook_confirm_delete.html"
    success_url = reverse_lazy("kitchen:cook-list")

    def test_func(self):
        return (self.request.user == self.get_object()
                or self.request.user.is_superuser)

    def handle_no_permission(self):
        context = {
            'action': 'delete',
        }
        return render(self.request, "kitchen/permission_denied.html", context)


class PermissionDeniedView(generic.TemplateView):
    template_name = "kitchen/permission_denied.html"


class DishListByTypeView(generic.ListView):
    template_name = 'kitchen/dish-list-by-type.html'
    context_object_name = 'dish_list'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        try:
            dish_type = DishType.objects.get(pk=pk)
            return Dish.objects.filter(dish_type=dish_type)
        except DishType.DoesNotExist:
            raise Http404("Dish Type does not exist.")
