from django.contrib import admin
from ingredients.models import Ingredients, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Ingredients)
