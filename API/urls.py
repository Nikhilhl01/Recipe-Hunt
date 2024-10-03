
from django.urls import path
from home.views import Recipe_API
urlpatterns = [
    path('Recipes/', Recipe_API.as_view()),
]
