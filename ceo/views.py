from django.shortcuts import get_object_or_404, render,HttpResponse,redirect
from django.urls import reverse
from django.views import generic
import json

from .models import *

#객체 반환
def get_object(model,**args):
    query_set = model.objects.filter(**args)
    return query_set[0] if query_set else None
def check_login(request,url):
    user_id = request.session.get('id')
    return user_id if user_id else redirect(url)
    
# Create your views here.
def main(request):
    recipes = Recipe.objects.all().order_by('-upload_date')
    
    return render(request,'main.html',{'recipes':recipes})
def detail_recipe(request):
    return render(request,'detail_recipe.html')    
# 로그인
def login(request):
    context = {}
    if request.method == "POST":
        user_id = request.POST.get('user_id')  
        user_pw = request.POST.get('user_pw')
        account = Account.objects.filter(user_id=user_id,password=user_pw)
        if account:
            request.session['id']=user_id
            return redirect('/')
        else:
            context['lgmsg'] = "아이디와 비밀번호가 일치하지 않습니다." 
    return render(request,'login.html',context)

#로그아웃 
def logout(request):
    del request.session['id']   
    return redirect('/')
# 회원가입 
def register(request):
    if request.method == "POST":
        Account.objects.create(
            user_id  = request.POST.get('user_id'),
            password = request.POST.get('user_pwd'),
            username = request.POST.get('user_name'),
            email    = request.POST.get('user_email'),
            phonenumber = request.POST.get('user_phone'),
        )
        return redirect('/login/')
    return render(request,'register.html')
#아이디 체크
def id_check(request):
    user_id = request.POST.get('id_check')
    account = Account.objects.filter(user_id=user_id)
    response = {}
    if account:
        response ={ 'msg' : True}
    else:
        response = {'msg' : False}
    print(response)
    return HttpResponse(json.dumps(response), content_type="application/json")

def manage_register(request):
    user_id = check_login(request,'/')
    account = get_object(Account,user_id=user_id)
    if account.level != 2: return render(request,'main.html',{'msg':'권한이 없습니다.'})  
    if request.method == "POST":
        Account.objects.create(
            user_id  = request.POST.get('user_id'),
            password = request.POST.get('user_pwd'),
            username = request.POST.get('user_name'),
            email    = request.POST.get('user_email'),
            phonenumber = request.POST.get('user_phone'),
            level      = 1
        )
        return redirect('/')

    return render(request,'manage_register.html')  
        
class ManagerRecipeView(generic.ListView):
    model = Recipe
    template_name = 'manage_recipe.html'


# class ManagerWriteRecipeView(generic.ListView):
#     model = Recipe
#     template_name = 'write_recipe.html'


def ManagerWriteRecipeView(request):
    user_id = check_login(request,'/')
    account = get_object(Account,user_id=id)
    #if account.level != 1 : return redirect('/')
    if request.method == "POST":
        print()
        recipe = Recipe.objects.create(
                    recipe_name=request.POST.get('title'),
                    rank = int(request.POST.get('rank')),
                    recipe_img_file_path = request.FILES.get('recipe_img'),
                    video_file_path = request.FILES.get('recipe_video'),
                    recipe_kind   = request.POST.get('kind')
                )
        
        url  = "media/recipe/doc/"+"recipe"+str(recipe.pk)+".html"
        url2 = "media/recipe/doc/"+"nutrition"+str(recipe.pk)+".html"
        with open(url, "w",encoding="UTF-8") as f:
            f.write(request.POST.get('recipe_info'))
        with open(url2,"w",encoding="UTF-8") as f:
            f.write(request.POST.get('info'))
        recipe.nutrition_document_file_path = url2 
        recipe.document_file_path = url
        recipe.save()
        for food in request.POST.get('food').split(','):
            food = food.replace(" ","")
            food_obj = get_object(Foodstuff,foodstuff_name=food)
            RFRealatoin.objects.create(
                recipe=recipe,
                foodstuff=food_obj
            )

    return render(request, 'write_recipe.html')

def manage_recipe(request):
    recipes = Recipe.objects.all().order_by('-upload_date')
    
    return render(request, 'manage_recipe.html',{'recipes':recipes})
def modify_recipe(request):
    pk = request.GET.get('id')
    recipe = get_object_or_404(Recipe,id=pk)
    realation_list = RFRealatoin.objects.filter(recipe=recipe)
    url = str(recipe.nutrition_document_file_path)
    url2= str(recipe.document_file_path)
    nur_doc = None
    rec_doc = None
    with open(url, "r",encoding="UTF-8") as f:
        nur_doc=f.read()
    with open(url2, "r",encoding="UTF-8") as f:
        rec_doc=f.read()    
    context = {
        'relation_list':realation_list,
        'recipe':recipe,
        'nur_doc':nur_doc,
        'rec_doc':rec_doc
    }
    return render(request, 'modify_recipe.html',context)
class ManagerStorageView(generic.ListView):
    model = Recipe
    template_name = 'manage_storage.html'


# class ManagerWriteStorageView(generic.ListView):
#     model = Recipe
#     template_name = 'write_storage.html'


def ManagerWriteStorageView(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'write_storage.html')