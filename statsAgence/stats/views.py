from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Article, handle_uploaded_file,Product,import_csv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def all_articles(request):
    all_articles=Article.objects.all()

    return render(request,"articles/all_articles.html",{"all_articles":all_articles,"model_name":"article","is_loading":True})
@csrf_exempt
def import_articles_(request,model_name):
    print(model_name)        
    if(request.method=="POST"):
        file_uploaded_name=handle_uploaded_file(request.FILES["articles"])
        import_csv(file_uploaded_name,model_name)
        return JsonResponse({"is_loaded":True})

def all_products(request):
    all_products=Product.objects.all()

    return render(request,"products/all_products.html",{"all_products":all_products,"model_name":"product","is_loading":True})
