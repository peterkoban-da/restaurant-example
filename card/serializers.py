from datetime import datetime, time

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from card.models import Dish, Drink


class ListDishSerializer(ModelSerializer):
    """
    Serializer
    """

    price = SerializerMethodField()
    name = SerializerMethodField()

    class Meta:
        """
        Meta
        """

        model = Dish
        fields = ["id", "name", "price"]

    def get_price(self, obj):
        """
        manipulates the price
        """
        current_time = datetime.now().time()
        if obj.lunch_action and time(10, 0) < current_time < time(14, 0):
            return f"{obj.price * 0.6} €"
        return f"{obj.price} €"

    def get_name(self, obj):
        """
        manipulates the name
        """
        if obj.is_vegan:
            return f"{obj.name} (vegan)"
        return obj.name


class ListDrinkSerializer(ModelSerializer):
    """
    Serializer for listing drinks
    """

    price = SerializerMethodField()
    name = SerializerMethodField()

    class Meta:
        """
        Meta
        """

        model = Drink
        fields = ["id", "name", "price"]

    def get_price(self, obj):
        """
        manipulates the price
        """
        current_time = datetime.now().time()
        if obj.lunch_action and time(10, 0) < current_time < time(12, 0):
            return f"{obj.price * 0.5} €"
        return f"{obj.price} €"

    def get_name(self, obj):
        """
        manipulates the name
        """
        if obj.is_alcoholic:
            return f"{obj.name} (Alkohol)"
        return obj.name


class CreateDrinkSerializer(ModelSerializer):
    """
    Serializer for creating Drinks
    """

    class Meta:
        """
        Meta
        """

        model = Drink
        fields = ["name", "price", "lunch_action", "is_alcoholic"]
