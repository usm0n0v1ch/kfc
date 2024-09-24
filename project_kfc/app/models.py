from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='dishes')
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order by {self.user.username}"


class OrderElement(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    dish_quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dish.name} x {self.dish_quantity}"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    dish_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username}'s basket: {self.dish.name} x {self.dish_quantity}"

