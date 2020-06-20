from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('manager/show/recipe', views.ManagerRecipeView.as_view(), name='show_recipe'),
    path('manager/write/recipe', views.ManagerWriteRecipeView.as_view(), name='write_recipe'),
    path('manager/show/storage', views.ManagerStorageView.as_view(), name='show_storage'),
    path('manager/write/storage', views.ManagerWriteStorageView.as_view(), name='write_storage'),
]