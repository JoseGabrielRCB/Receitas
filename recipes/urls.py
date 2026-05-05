"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.home,name='recipes-home'),
    path('recipes/<int:id>/',views.recipe,name='recipes-recipe'),
]


# path('recipes/<id>/',views.recipe) captura dnnamicamente os valores recipes/1..2..3....
# nescessário atulizar parametro em views 

# https://docs.djangoproject.com/en/6.0/topics/http/urls/