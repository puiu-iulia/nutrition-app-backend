from rest_framework import serializers

from ..models import MealPlan
from ..serializers import MealDetailsSerializer


class MealPlanSerializer(serializers.ModelSerializer):
    """Serializer for daily meal plan"""

    class Meta:
        model = MealPlan
        fields = ('id', 'date', 'meals')
        read_only_fields = ('id',)


class MealPlanDetailsSerializer(serializers.ModelSerializer):

    meals = MealDetailsSerializer(many=True)

    class Meta:
        model = MealPlan
        fields = ('id', 'date', 'meals')
        read_only_fields = ('id',)
