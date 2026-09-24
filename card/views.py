from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from card.models import Dish, Drink
from card.serializers import (
    CreateDrinkSerializer,
    ListDishSerializer,
    ListDrinkSerializer,
)


class ListDishView(APIView):
    """
    View to list all dishes
    """

    def get(self, request):
        """
        GET
        """
        dishes = Dish.objects.all()
        serializer = ListDishSerializer(dishes, many=True)
        return Response(serializer.data)


class ListDrinkView(APIView):
    """
    View to list all drinks
    """

    def get(self, request):
        """
        GET
        """
        drinks = Drink.objects.all()
        serializer = ListDrinkSerializer(drinks, many=True)
        return Response(serializer.data)


class CreateDrinkView(APIView):
    """
    View to list all drinks
    """

    def post(self, request):
        """
        Post
        """
        serializer = CreateDrinkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        drink = serializer.save()
        return Response(
            CreateDrinkSerializer(drink).data,
            status=status.HTTP_201_CREATED,
        )
