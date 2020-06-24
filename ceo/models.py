from django.db import models
from datetime import datetime

# Create your models here.

class Account(models.Model):
    # 계정 모델
    user_id = models.CharField(max_length = 16, db_index = True, unique = True) # 계정
    password = models.CharField(max_length = 32) # 비밀번호
    username = models.CharField(max_length = 32) # 닉네임
    email = models.CharField(max_length = 64, db_index = True) # 이메일
    phonenumber = models.CharField(max_length = 15) # 전화번호
    level = models.IntegerField(default = 0) # 등급 


class Recipe(models.Model):
    # 레시피 모델
    recipe_name = models.CharField(max_length = 100, db_index = True, unique = True) # 레시피 제목
    rank = models.IntegerField(default=0) # 난이도
    recommendation = models.IntegerField(default=0) # 추천수
    upload_date = models.DateField(auto_now_add=True) # 작성날짜
    recipe_kind = models.CharField(max_length = 10,null=True,blank=True) #종류
    recipe_img_file_path = models.ImageField(upload_to="recipe/img/",null=True,blank=True) # 레시피 완성 요리 이미지 파일 주소
    nutrition_document_file_path = models.CharField(max_length = 300,null=True,blank=True) # 영양정보
    video_file_path = models.FileField(upload_to="recipe/video/", null=True,blank=True) # 동영상 파일주소
    document_file_path = models.FileField() # 문서 파일주소


class Foodstuff(models.Model):
    # 제료 정보 모델
    foodstuff_name = models.CharField(max_length = 100, db_index = True, unique = True)
    price = models.IntegerField()


class RFRealatoin(models.Model):
    # 레시피, 재료 다대다 관계를 위한 모델
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    foodstuff = models.ForeignKey(Foodstuff, on_delete = models.CASCADE)

    
class FSStorage(models.Model):
    # 재료 보관법 모델
    foodstuff = models.OneToOneField(Foodstuff,on_delete=models.CASCADE,null=True,blank=True)
    storage_name = models.CharField(max_length = 100, db_index = True, unique = True)
    fss_img_file_path = models.ImageField(upload_to="fs_storage/img/",null=True,blank=True)
    storage_file_path = models.CharField(max_length = 300)
