from django.contrib import admin

from card.models import Dish, Drink


@admin.register(Dish)
class AdminDish(admin.ModelAdmin):
    pass


@admin.register(Drink)
class AdminDrink(admin.ModelAdmin):
    pass
