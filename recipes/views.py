from django.shortcuts import render
from django.http  import HttpResponse
 
def home(request):
    return render(request,'recipes/home.html',
                  status=201,
                  context={'name' : 'Jose gabriel'})
