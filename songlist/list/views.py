from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'list/index.html', {'articles': articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'list/article_page.html', {'article': article})

def edit_page(request):
    return render(request, 'list/edit_page.html')

def edit_action(request):
    song_name = request.POST.get('song_name', 'song_name')
    singer = request.POST.get('singer', 'singer')
    models.Article.objects.create(song_name=song_name, singer=singer)
    articles = models.Article.objects.all()
    return render(request, 'list/index.html', {'articles': articles})