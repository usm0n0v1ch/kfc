from django import forms

from app.models import Category, Dish


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'