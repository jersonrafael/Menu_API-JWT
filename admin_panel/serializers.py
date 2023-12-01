from rest_framework import serializers

from .models import *
from accounts.models import *


class plateSerializer(serializers.ModelSerializer):
    class Meta:
        model = plate
        fields = '__all__'

class alterplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = plate
        fields = [
            "name",
            "price",
            "ingredient",
            "image",
            "category"
        ]

class drinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = drink
        fields = '__all__'

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields= '__all__'
