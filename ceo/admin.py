from django.contrib import admin
from .models import Account, Recipe, Foodstuff, FSStorage

# Register your models here.
admin.site.register(Account)
admin.site.register(Recipe)
admin.site.register(Foodstuff)
admin.site.register(FSStorage)