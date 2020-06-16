from django.db import models
from datetime import datetime

# Create your models here.

class Account(models.Model):
    user_id = models.CharField(max_length = 16, db_index = True, unique = True)
    password = models.CharField(max_length = 32)
    username = models.CharField(max_length = 32, unique = True)
    email = models.CharField(max_length = 64, db_index = True)
    phonenumber = models.CharField(max_length = 15)
    level = models.IntegerField()


class Recipe(models.Model):
    recipe_name = models.CharField(max_length = 100, db_index = True, unique = True)
    rank = models.IntegerField()
    recommendation = models.IntegerField()
    upload_date = models.DateField(db_column = datetime.now().strftime('%Y-%m-%d'))
    nutrition_document_file_path = models.CharField(max_length = 300)
    video_file_path = models.CharField(max_length = 300)
    document_file_path = models.CharField(max_length = 300)


class Foodstuff(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.PROTECT)
    foodstuff_name = models.CharField(max_length = 100, db_index = True, unique = True)
    price = models.IntegerField()

class FSStorage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.PROTECT)
    storage_name = models.CharField(max_length = 100, db_index = True, unique = True)
    storage_file_path = models.CharField(max_length = 300)
