from django.shortcuts import get_object_or_404, render,HttpResponse,redirect
from django.urls import reverse
from django.views import generic
import json
from .file_func import create_file
from django.contrib import messages

from .models import *

#객체 반환
def get_object(model,**args):
    query_set = model.objects.filter(**args)
    return query_set[0] if query_set else None


# 로그인 체크
def isLogin(request,**args):
    
    if not request.session.get('id'): 
        messages.info(request, '로그인 하세요.')
        return '/login'
    if args.get('level'):    
        account = get_object(Account,user_id=request.session.get('id'))
        if  account.level != args.get('level'): 
            messages.info(request, '권한이 없습니다.')
            return '/' 
            

# Create your views here.
def main(request):
    recipes = Recipe.objects.all().order_by('-upload_date')
    
    return render(request,'main.html',{'recipes':recipes})


#레시피 상세보기    
def detail_recipe(request,num):
    recipe = get_object_or_404(Recipe,id=num)
    realations = RFRealatoin.objects.filter(recipe=recipe)
    storage = []
    for realation in realations:
        try:
            obj = realation.foodstuff.fsstorage
            storage.append(obj)
        except Exception as e:
            pass        

    
    context = {
        'recipe':recipe,
        'realations':realations,
        'storage':storage
    }
    return render(request,'detail_recipe.html',context)   


# 로그인
def login(request):
    context = {}
    if request.method == "POST":
        user_id = request.POST.get('user_id')  
        user_pw = request.POST.get('user_pw')
        account = Account.objects.filter(user_id=user_id,password=user_pw)
        if account:
            request.session['id']=user_id
            request.session['level']=account[0].level
            return redirect('/')
            
        else:
            messages.info(request, '아이디와 비밀번호 일치하지 않습니다.')
            return redirect('/login')
        
    return render(request,'login.html',context)


#로그아웃 
def logout(request):
    del request.session['id']   
    del request.session['level']   
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
# 아이디 체크
def id_check(request):
    user_id = request.POST.get('id_check')
    account = Account.objects.filter(user_id=user_id)
    response = {}
    if account:
        response ={ 'msg' : False}
    else:
        response = {'msg' : True}

    return HttpResponse(json.dumps(response), content_type="application/json")


# 관리자 등록
def manage_register(request):
    path = isLogin(request,level=2)
    if path : return redirect(path)
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


# 레시피 작성    
def ManagerWriteRecipeView(request):
    path = isLogin(request,level=1)
    if path : return redirect(path)

    if request.method == "POST":
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
        return redirect('/manager/show/recipe')
    return render(request, 'write_recipe.html')


# 레시피 관리
def manage_recipe(request):
    path = isLogin(request,level=1)
    if path : return redirect(path)
    recipes = Recipe.objects.all().order_by('-upload_date')
    return render(request, 'manage_recipe.html',{'recipes':recipes})


# 레시피 수정 뷰함수인데 구현에 예상치 못 한 에러 발생해서 추후 확인 후 구현하기.
# def modify_recipe(request):
#     path = isLogin(request,level=1)
#     if path : return redirect(path)
#     pk = request.GET.get('id')
#     recipe = get_object_or_404(Recipe,id=pk)
#     realation_list = RFRealatoin.objects.filter(recipe=recipe)
#     url = str(recipe.nutrition_document_file_path)
#     url2= str(recipe.document_file_path)
#     nur_doc = None
#     rec_doc = None
#     with open(url, "r",encoding="UTF-8") as f:
#         nur_doc=f.read()
#     with open(url2, "r",encoding="UTF-8") as f:
#         rec_doc=f.read()    
#     context = {
#         'relation_list':realation_list,
#         'recipe':recipe,
#         'nur_doc':nur_doc,
#         'rec_doc':rec_doc
#     }
#     return render(request, 'modify_recipe.html',context)


# 재료 보관 방법 관리
def ManagerStorageView(request):
    path = isLogin(request,level=1)
    if path : return redirect(path)
    fsstorages = FSStorage.objects.all()
    return render(request, 'manage_storage.html', {'fsstorages' : fsstorages})


# 재료 보관 방법 등록
def ManagerWriteStorageView(request):
    path = isLogin(request,level=1)
    if path : return redirect(path)

    if request.method == 'POST':
        
        fds = FSStorage.objects.filter(foodstuff = request.POST.get('storageName'))

        if fds:
            response = {'confirm' : False, 'msg' : "작성된 보관법입니다."}            
        else:
            fds = Foodstuff.objects.filter(id = request.POST.get('storageName'))
            filepath = create_file(fds[0].foodstuff_name, request.POST.get('storageDoc'))

            FSStorage.objects.create(
                foodstuff_id = request.POST.get('storageName'),
                storage_name = fds[0].foodstuff_name,
                fss_img_file_path = request.FILES.get('storageImg'),
                storage_file_path = filepath
            )
            response = {'confirm' : True}

        return HttpResponse(json.dumps(response), content_type="application/json")

    foodstuffs = Foodstuff.objects.all()

    return render(request, 'write_storage.html', {'foodstuffs' : foodstuffs})


# 남은 재료 보관 방법
def StorageShowListView(request):
    
    fsstorages = FSStorage.objects.all()
    if not fsstorages:
        messages.info(request, '재료 보관방법이 없습니다.')
        return redirect('/')

    return render(request, 'remain_foodstuff_storage_list.html', {'fsstorages' : fsstorages})


#  재료 보관 방법
def StorageDetailView(request, id):
    
    fss = FSStorage.objects.get(id = id)
    if not fss:
        messages.info(request, '해당 재료 보관방법이 없습니다.')
        return redirect('/')

    return render(request, 'show_storage.html', {"fsstorage" : fss})