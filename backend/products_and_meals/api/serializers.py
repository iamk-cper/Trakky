from rest_framework import serializers
from products_and_meals.models import (Product, Summary, Demand, Meal, MealItem)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'

class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class MealItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealItem
        fields = '__all__'