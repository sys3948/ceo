from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('manager/show/recipe', views.ManagerRecipeView.as_view(), name='show_recipe'),
    path('manager/write/recipe', views.ManagerWriteRecipeView, name='write_recipe'),
    path('manager/show/storage', views.ManagerStorageView.as_view(), name='show_storage'),
    path('manager/write/storage', views.ManagerWriteStorageView.as_view(), name='write_storage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)