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
    path('detail_recipe/<num>/',views.detail_recipe,name="detail_recipe"),
    path('manage/register/',views.manage_register,name="manage_register"),
    path('manager/write/recipe', views.ManagerWriteRecipeView, name='write_recipe'),
    # path('manager/modify/recipe', views.modify_recipe, name='modify_recipe'),
    path('manager/show/recipe', views.manage_recipe, name='manage_recipe'),
    path('manager/show/storage', views.ManagerStorageView, name='show_storage'),
    path('manager/write/storage', views.ManagerWriteStorageView, name='write_storage'),
    path('show/storage', views.StorageShowListView, name='show_storage_list'),
    path('show/storage/<int:id>', views.StorageDetailView, name='show_storage_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)