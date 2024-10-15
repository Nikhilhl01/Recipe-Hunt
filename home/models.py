from django.db import models

# Create your models here.

class Recipe(models.Model):
  recipe_name = models.CharField(max_length = 100, db_index = True)
  recipe_desc = models.TextField()
  recipe_img = models.ImageField( upload_to="recipe/")
  recipe_type = models.CharField(max_length = 100, choices =(("Veg", "Veg"),("Non-Veg", "Non-Veg")) )
  recipe_slug = models.SlugField(unique = True)

class Ingredients(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name = "recipe_ingreidents")
  ingredent_name = models.CharField(max_length = 100)