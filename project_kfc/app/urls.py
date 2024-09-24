from django.urls import path

from app import views
from app.views import PanelView, MenuView, CategoryView, DishView, UserView, CategoryUpdateView, DishUpdateView, \
    CategoryDetailView, DishDetailView, CategoryCreateView, CategoryDeleteView, DishCreateView, DishDeleteView

urlpatterns = [
    path('panel/', PanelView.as_view(), name='panel'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('category/', CategoryView.as_view(), name='category'),
    path('dish/', DishView.as_view(), name='dish'),
    path('user/', UserView.as_view(), name='user'),
    path('edit_category/<int:pk>/', CategoryUpdateView.as_view(), name='edit_category'),
    path('edit_dish/<int:pk>/', DishUpdateView.as_view(), name='edit_dish'),
    path('detail_category/<int:pk>/', CategoryDetailView.as_view(), name='detail_category'),
    path('detail_dish/<int:pk>/', DishDetailView.as_view(), name='detail_dish'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('delete_category/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
    path('create_dish/', DishCreateView.as_view(), name='create_dish'),
    path('delete_dish/<int:pk>/', DishDeleteView.as_view(), name='delete_dish'),
    path('add_to_basket/<int:dish_id>/', views.add_to_basket, name='add_to_basket'),
    path('basket/', views.basket_view, name='basket'),
    path('create-order/', views.create_order, name='create_order'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
    path('basket/decrease/<int:item_id>/', views.decrease_quantity_in_basket, name='decrease_quantity_in_basket'),
]