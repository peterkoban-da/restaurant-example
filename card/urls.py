from django.urls import path

from card.views import CreateDrinkView, ListDishView, ListDrinkView

urlpatterns = [
    path("dishes/", ListDishView.as_view()),
    path("drinks/", ListDrinkView.as_view()),
    path("drinks/create", CreateDrinkView.as_view()),
]
