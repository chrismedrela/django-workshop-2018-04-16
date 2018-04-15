from django.forms import ModelForm

from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ('slug', 'author', 'date_created', 'date_updated')