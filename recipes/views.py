from django.shortcuts import render
from django.http  import HttpResponse
from recipes.utils.recipes.factory import make_recipe 
 
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'José Gabril',
        'recipes': [make_recipe() for _ in range(10)],
    })

def recipe(request,id):
    return render(request,'recipes/pages/recipe-view.html',
                  status=201,
                  context={'recipes': make_recipe(),
                           })
