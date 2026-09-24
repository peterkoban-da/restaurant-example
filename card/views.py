from rest_framework.response import Response
from rest_framework.views import APIView

from card.models import Dish
from card.serializers import ListDishSerializer


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
