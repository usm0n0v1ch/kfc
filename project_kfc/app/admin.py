from django.contrib import admin

from app.models import Category, Dish, Order, OrderElement, Basket

# Register your models here.


admin.site.register([Category,Dish,Order,OrderElement,Basket])