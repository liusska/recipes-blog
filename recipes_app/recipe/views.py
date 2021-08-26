from django.shortcuts import render, redirect
from recipes_app.recipe.models import Recipe
from recipes_app.recipe.forms import RecipeForm
from recipes_app.recipe.forms import DeleteRecipeForm


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()
    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def detail_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }

    return render(request, 'details.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe.save()
            return redirect('index')
    else:
        form = RecipeForm(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteRecipeForm(request.POST, instance=recipe)
        recipe.delete()
        return redirect('index')
    else:
        form = DeleteRecipeForm(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'delete.html', context)
