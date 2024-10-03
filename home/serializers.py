from rest_framework import serializers
from .models import Recipe, Ingredients

class IngredientsSerializers(serializers.ModelSerializer):
  class Meta:
    model = Ingredients
    fields = '__all__'



class RecipeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recipe
    fields = '__all__'

  def to_representation(self, instance):
    data = super().to_representation(instance)
    data["ingredients"]= IngredientsSerializers( instance.recipe_ingredents.all(), many = True).data

    return data


