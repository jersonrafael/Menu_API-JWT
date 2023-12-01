from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *

from admin_panel.models import *

from django.shortcuts import get_object_or_404


# Create your views here.
class categorysView(APIView):
    def get(self,request):
        model = category.objects.all()
        serializer = categorySerializer(model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class categoryView(APIView):
    def get(self,request,pk):
        model = get_object_or_404(category, pk=pk)
        serializer = categorySerializer(model)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class platesView(APIView):
    def get(self,request):
        model = plate.objects.all()
        serializer = productSerializer(model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class plateView(APIView):
    def get(self,request,pk):
        model = get_object_or_404(plate, pk=pk)
        serializer = productSerializer(model)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class filterProductByCategory(APIView):
    def get(self,request,pk):
        model = plate.objects.filter(category=pk) 
        serializer = productSerializer(model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class drinksView(APIView):
    def get(self,request):
        model = drink.objects.all()
        serializer = drinkSerializer(model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class drinkView(APIView):
    def get(self,request,pk):
        model = get_object_or_404(drink,pk=pk)
        serializer = drinkSerializer(model)
        return Response(serializer.data,status=status.HTTP_200_OK)