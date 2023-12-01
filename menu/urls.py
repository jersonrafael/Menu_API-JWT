from django.urls import path
from .views import *

urlpatterns = [
    path('categorys/', categorysView.as_view(), name='categorys'),
    path('category/<int:pk>/', categoryView.as_view(), name='category'),
    path('category/product/<int:pk>/', filterProductByCategory.as_view(), name='filterProduct'),

    path('plates/', platesView.as_view(), name='products'),
    path('plate/<int:pk>/', plateView.as_view(), name='product'),

    path('drinks/', drinksView.as_view(), name='drinks'),
    path('drink/<int:pk>/', drinkView.as_view(), name='drink'),
]
