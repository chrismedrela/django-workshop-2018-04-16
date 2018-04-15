import logging

from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView

from .forms import RecipeForm
from .models import Recipe


logger = logging.getLogger(__name__)


class RecipeListView(ListView):
    template_name = 'recipes/index.html'
    paginate_by = 5

    def get_queryset(self):
        recipes = Recipe.objects.all()
        logger.debug('Recipes count: %d' % recipes.count())
        return recipes


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipes/form.html'
    form_class = RecipeForm

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.author = self.request.user
        recipe.slug = slugify(recipe.title)
        recipe.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = True
        return context  


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/form.html'
    pk_url_kwarg = 'recipe_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = False
        return context

    def form_valid(self, form):
        retval = super().form_valid(form)
        messages.success(self.request, 'The recipe was updated.')
        return retval
        
    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user or self.request.user.is_staff
