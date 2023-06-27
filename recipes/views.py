from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    context = {'recipes': recipes}
    return render(request, 'recipes/pages/home.html', context=context)


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    context = {'recipes': recipes}
    return render(request, 'recipes/pages/home.html', context=context)


def recipe(request, id):
    context = {'recipes': [make_recipe()], 'is_detail_page': True}
    return render(request, 'recipes/pages/recipe-view.html', context=context)
