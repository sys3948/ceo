from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Account, Recipe, Foodstuff, FSStorage

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'main.html'

    def get_queryset(self):
        Recipe.objects.order_by('upload_date')


class LoginView(generic.ListView):
    model = Account
    template_name = "login.html"


class RegisterView(generic.ListView):
    model = Account
    template_name = "register.html"


class ManagerRecipeView(generic.ListView):
    model = Recipe
    template_name = 'manage_recipe.html'


# class ManagerWriteRecipeView(generic.ListView):
#     model = Recipe
#     template_name = 'write_recipe.html'


def ManagerWriteRecipeView(request):
    if not request.session.get('id'):
        # redirect 하기!
        print('None Session!!')
    
    return render(request, 'write_recipe.html')


class ManagerStorageView(generic.ListView):
    model = Recipe
    template_name = 'manage_storage.html'


class ManagerWriteStorageView(generic.ListView):
    model = Recipe
    template_name = 'write_storage.html'