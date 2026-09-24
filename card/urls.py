from django.urls import path

from card.views import ListDishView

urlpatterns = [path("dishes/", ListDishView.as_view())]
