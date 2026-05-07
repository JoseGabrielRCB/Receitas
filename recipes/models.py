from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=50)


class Recipe(models.Model):
    #Campos Base
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    descipition = models.CharField(max_length=1000)
    serving = models.CharField( max_length=50)
    servings_unit = models.CharField(max_length=50)
    preparation_time = models.IntegerField
    preparation_time_unit = models.CharField(max_length=50)
    preparation_time_is_html = models.BooleanField(default=False)
    preparation_steps = models.TextField()
    creat_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/cover/%Y/%m/%d/') #salvar o local em data especifica

    # Relacoes
    Category= models.ForeignKey(Category,on_delete=models.SET_NULL,null=True) # Caso seja deletado, seta como NULL
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)
