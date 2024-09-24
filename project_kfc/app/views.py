from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView

from app.forms import CategoryForm, DishForm
from app.models import Category, Dish, Order, Basket, OrderElement


# Create your views here.


class PanelView(TemplateView):
    template_name = "app/admin/panel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My Custom Page'
        return context


class CategoryView(TemplateView):
    template_name = "app/admin/category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        return context

class DishView(TemplateView):
    template_name = "app/admin/dish.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dishes']=Dish.objects.all()
        return context


class UserView(TemplateView):
    template_name = "app/admin/user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['orders'] = Order.objects.select_related('user').all()
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'app/admin/edit_category.html'
    success_url = reverse_lazy('category')

    def get_object(self, queryset=None):
        return super().get_object(queryset)





class DishUpdateView(UpdateView):
    model = Dish
    form_class = DishForm
    template_name = 'app/admin/edit_dish.html'
    success_url = reverse_lazy('dish')

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class CategoryDetailView(TemplateView):
    template_name = "app/admin/detail_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category']=Category.objects.get(id=self.kwargs['pk'])
        return context

class DishDetailView(TemplateView):
    template_name = "app/admin/detail_dish.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish']=Dish.objects.get(id=self.kwargs['pk'])
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'app/admin/create_category.html'
    success_url = reverse_lazy('category')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'app/admin/delete_category.html'
    success_url = reverse_lazy('category')

class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'app/admin/create_dish.html'
    success_url = reverse_lazy('dish')

class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'app/admin/delete_dish.html'
    success_url = reverse_lazy('dish')


class MenuView(TemplateView):
    template_name = "app/customer/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def basket_view(request):
    basket_items = Basket.objects.filter(user=request.user)

    total_price = 0
    for item in basket_items:
        item.total_price = item.dish.price * item.dish_quantity
        total_price += item.total_price

    return render(request, 'app/customer/basket.html', {'basket_items': basket_items, 'total_price': total_price})
def add_to_basket(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)

    basket_item, created = Basket.objects.get_or_create(
        user=request.user,
        dish=dish,
        defaults={'dish_quantity': 0}
    )

    basket_item.dish_quantity += 1
    basket_item.save()

    return redirect('menu')


def create_order(request):
    basket_items = Basket.objects.filter(user=request.user)
    if basket_items.exists():
        new_order = Order.objects.create(user=request.user)
        for item in basket_items:
            OrderElement.objects.create(
                order=new_order,
                dish=item.dish,
                dish_quantity=item.dish_quantity
            )

        basket_items.delete()
    return redirect('order_confirmation')

def order_confirmation(request):
    return render(request, 'app/customer/order_confirmation.html')


def decrease_quantity_in_basket(request, item_id):

    basket_item = get_object_or_404(Basket, id=item_id, user=request.user)
    if basket_item.dish_quantity > 1:
        basket_item.dish_quantity -= 1
        basket_item.save()
    else:
        basket_item.delete()
    return redirect('basket')