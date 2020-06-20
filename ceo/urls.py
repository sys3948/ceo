from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('idCheck/',views.id_check,name="idCheck"),
    path('detail_recipe/',views.detail_recipe,name="detail_recipe"),
    path('manage/register/',views.manage_register,name="manage_register"),
    path('manager/show/recipe', views.ManagerRecipeView.as_view(), name='show_recipe'),
    path('manager/write/recipe', views.ManagerWriteRecipeView, name='write_recipe'),
    path('manager/modify/recipe', views.modify_recipe, name='modify_recipe'),
    path('manager/manage/recipe', views.manage_recipe, name='manage_recipe'),
    path('manager/show/storage', views.ManagerStorageView.as_view(), name='show_storage'),
    path('manager/write/storage', views.ManagerWriteStorageView, name='write_storage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)