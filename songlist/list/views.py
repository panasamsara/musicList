from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models

def index(request):
    # articles_list = models.Article.objects.all()
    # paginator = Paginator(articles_list, 25)# Show 25 contacts per page
    # page = request.GET.get('page')
    # try:
    #     articles = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     articles = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     articles = paginator.page(paginator.num_pages)
    articles = models.Article.objects.all()
    return render(request, 'list/index.html', {'articles': articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'list/article_page.html', {'article': article})

def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'list/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'list/edit_page.html', {'article': article})


def edit_action(request):
    article_id = request.POST.get('article_id', '0')
    song_name = request.POST.get('song_name', '歌名')
    singer = request.POST.get('singer', '歌手')
    if article_id == "0":
        models.Article.objects.create(song_name=song_name, singer=singer)
        # articles = models.Article.objects.all()
        # return render(request, 'list/index.html', {'articles': articles})
        return HttpResponseRedirect('/list/index')

    article = models.Article.objects.get(pk=article_id)
    article.song_name = song_name
    article.singer = singer
    article.save()
    return render(request, 'list/article_page.html', {'article': article})