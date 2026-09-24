from django.db import models


# Create your models here.
class CardItem(models.Model):
    """
    Model for basic Card Item
    """

    name = models.CharField(max_length=150)
    price = models.FloatField()
    lunch_action = models.BooleanField(default=False)


class Dish(CardItem):
    """
    Model for Dish
    """

    is_vegan = models.BooleanField(default=False)


class Drink(CardItem):
    """
    Model for Drinks
    """

    is_alcoholic = models.BooleanField(default=False)
