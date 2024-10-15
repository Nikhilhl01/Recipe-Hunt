from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RecipeSerializer , CreateRecipeSerializer
from .models import Recipe, Ingredients


class Recipe_API(APIView):
  def get(self , request):
    queryset = Recipe.objects.all()
    serializers = RecipeSerializer(queryset, many = True)
    
    return Response({
      "status" : True,
      "Message": "data fetched",
      "data" : serializers.data
    })

def post(self, request):
    data = request.data
    serializer = CreateRecipeSerializer(data=data )
    if not serializer.is_valid():
       return Response({
        "status" : True,
        "Message": "data not created",
        "data" : serializer.errors
      })
    serializer.save()
    return Response({
    "status" : True,
    "Message": "data created",
    "data" : {}
  })


def delete(self, request):
    data = request.data
    recipe= Recipe.objects.get(id = data.get('id'))
    if recipe.exixt():
      recipe.delete()
      return Response({
       "status" : True,
       "Message": "data deleted",
       "data" : {}
      })
    
    return Response({
    "status" : True,
    "Message": "invalid id",
    "data" : {}
  })

