from rest_framework.serializers import ModelSerializer

from card.models import Dish, Drink


class ListDishSerializer(ModelSerializer):
    """
    Serializer
    """

    class Meta:
        """
        Meta
        """

        model = Dish
        fields = ["id", "name", "price"]
