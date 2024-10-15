from rest_framework import serializers
from .models import Recipe, Ingredients
from django.template.defaultfilter import slugfy
import uuid

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

class CreateRecipeSerializer(serializers.ModelSerializer):
  reirecipe_ingreidents = serializers.ListField(
    child = serializers.CharField()
  )
  class Meta:
    model = Recipe
    fields = '__all__'
    
    
def create(self, validated_data):
  recipe_slug = slugfy(validated_data['recipe_name'])
  if Recipe.objects.filter(recipe_slug = recipe_slug).exist():
    recipe_slug= f"{recipe_slug}_{str(uuid.uuid4()).split('-')[0]}"
  recipe = Recipe.objects.create(
      recipe_name = validated_data['recipe_name'],
      recipe_desc = validated_data['recipe_desc'],
      recipe_slug = validated_data['recipe_slug'],
      recipe_img = validated_data['recipe_img'],
      recipe_type = validated_data['recipe_type']
    
  )

  for i in validated_data.get('reirecipe_ingreidents'):
    Ingredients.objects.create(
      recipe = recipe,
      ingredent_name = i
    )
    
  return recipe

