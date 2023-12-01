from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from .models import *
from .serializers import *
from accounts.models import *

# Create your views here.
class platesView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        model = plate.objects.all()
        serializer = plateSerializer(model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = plateSerializer(data=request.data)
        if serializer.is_valid():
            product_name = serializer.validated_data['name']
            if plate.objects.filter(name=product_name).exists():
                return Response({"detail": "That product already exist"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class getPlateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        model = get_object_or_404(plate,pk=pk)
        serializer = plateSerializer(model)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def patch(self,request,pk):
        model = get_object_or_404(plate,pk=pk)
        serializer = alterplateSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk):
        model = get_object_or_404(plate,pk=pk)
        serializer = alterplateSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        model = get_object_or_404(plate,pk=pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class categorysView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        model = category.objects.all()
        serializer = categorySerializer(model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = categorySerializer(data=request.data)
        if serializer.is_valid():
            find = category.objects.filter(name=serializer.validated_data["name"])
            if find:
                return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            

class categoryView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        model = get_object_or_404(category,pk=pk)
        serializer = categorySerializer(model)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def patch(self,request,pk):
        model = get_object_or_404(category,pk=pk)
        serializer = categorySerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        model = get_object_or_404(category,pk=pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class drinksView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        model = drink.objects.all()
        serializer = drinkSerializer(model,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = drinkSerializer(data=request.data)
        if serializer.is_valid():
            drink_name = serializer.validated_data["name"]
            if drink.objects.filter(name=drink_name).exists():
                return Response({"message":"That drink already exist"},status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
class drinkView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        model = get_object_or_404(drink,pk=pk)
        serializer = drinkSerializer(model)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def patch(self,request,pk):
        model = get_object_or_404(drink,pk=pk)
        serializer = drinkSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   

    def delete(self,request,pk):
        model = get_object_or_404(drink,pk=pk)
        model.delete()
        return Response({"message":"Drink has been deleted"}, status=status.HTTP_204_NO_CONTENT)


class registerView(APIView):

    def post(self,request):
        data = request.data 
        user = CustomUser.objects.create(
            username=data["username"],
            email = data["email"],
            password = make_password(data["password"])
        )
        if user != None :
            return Response({"message":"user created"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"Error"}, status=status.HTTP_400_BAD_REQUEST)
