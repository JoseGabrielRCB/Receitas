from django.db import models

# Create your models here.

# EDITED
# title description slug
# preparation_time preparation_time_unit
# servings servings_unit
# preparation_step
# preparation_step_is_html
# created_at updated_at
# is_published
# cover
# category (Relação)
# Author (Relação)

class Recipe(models.Model):
    title = models.models.CharField(max_length=50)
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
    
