from django.shortcuts import render
from .models import Article
from django.shortcuts import render, redirect

def all_articles(request):
    all_articles=Article.objects.all()

    return render(request,"articles/all_articles.html",{"all_articles":all_articles})