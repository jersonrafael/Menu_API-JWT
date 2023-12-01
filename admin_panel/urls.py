from django.urls import path

from .views import *

urlpatterns = [
    path('plates/', platesView.as_view(), name='plates'),
    path('plate/<int:pk>/',getPlateView.as_view(),name='plate'),

    path('categorys/', categorysView.as_view(), name='categorys'),
    path('category/<int:pk>/',categoryView.as_view(),name='product'),

    path('drinks/', drinksView.as_view(), name='drinks'),
    path('drink/<int:pk>/',drinkView.as_view(),name='drink'),
    
    path('register/', registerView.as_view(), name='register'),
]
