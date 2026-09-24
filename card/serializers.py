from datetime import datetime, time

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from card.models import Dish, Drink


class ListDishSerializer(ModelSerializer):
    """
    Serializer
    """

    price = SerializerMethodField()

    class Meta:
        """
        Meta
        """

        model = Dish
        fields = ["id", "name", "price"]

    def get_price(self, obj):
        """
        get
        """
        current_time = datetime.now().time()
        if obj.lunch_action and time(10, 0) < current_time < time(14, 0):
            return f"{obj.price * 0.6} €"
        return f"{obj.price} €"
