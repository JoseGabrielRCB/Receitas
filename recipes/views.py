from django.shortcuts import render
from django.http  import HttpResponse
 
def home(request):
    return render(request,'recipes/pages/home.html',
                  status=201,
                  context={'name' : 'Jose gabriel'})

def recipe(request,id):
    return render(request,'recipes/pages/recipe-view.html',
                  status=201,
                  context={'name' : 'Jose gabriel'})
