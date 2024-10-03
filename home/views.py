from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RecipeSerializer
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