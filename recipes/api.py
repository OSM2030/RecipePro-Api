from ninja import Router
from .models import Recipe
from django.shortcuts import get_object_or_404
from typing import List
from pydantic import BaseModel

recipeRouter = Router()

class RecipeSchema(BaseModel):
    name: str
    ingredients: str
    cooking_steps: str

@recipeRouter.get("/", response=List[RecipeSchema])
def get_recipes(request):
    return list(Recipe.objects.values("name", "ingredients", "cooking_steps"))

@recipeRouter.post("/")
def add_recipe(request, payload: RecipeSchema):
    recipe = Recipe.objects.create(**payload.dict())
    return {"id": recipe.id, "message": "Recipe added successfully!"}

@recipeRouter.get("/{recipe_id}", response=RecipeSchema)
def get_recipe(request, recipe_id: int):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return {"name": recipe.name, "ingredients": recipe.ingredients, "cooking_steps": recipe.cooking_steps}

@recipeRouter.put("/{recipe_id}")
def update_recipe(request, recipe_id: int, payload: RecipeSchema):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    for attr, value in payload.dict().items():
        setattr(recipe, attr, value)
    recipe.save()
    return {"message": "Recipe updated successfully!"}

@recipeRouter.delete("/{recipe_id}")
def delete_recipe(request, recipe_id: int):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return {"message": "Recipe deleted successfully!"}
