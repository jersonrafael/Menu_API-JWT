from rest_framework import serializers

from admin_panel import models

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.category
        fields = [
            "id",
            "name"
        ]

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.plate
        fields = "__all__"


class drinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.drink
        fields = "__all__"