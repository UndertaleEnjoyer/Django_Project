from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import CreateArticle
from django.shortcuts import HttpResponse
from . import forms

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_item(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_item.html', {'article': article})


@login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('homepage')
    else:
        form = CreateArticle()
    return render(request, template_name='articles/article_form.html', context={'form': form})

@login_required(login_url='accounts:login')
def article_update(request, slug):
    article = Article.objects.get(slug=slug)
    if request.user.id == article.author.id:
        if request.method == 'POST':
            form = forms.CreateArticle(request.POST, request.FILES, instance=article)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('articles:article_detail', slug=article.slug)
        else:
            form = forms.CreateArticle(instance=article)
        return render(request, template_name='articles/article_form.html', context={'form': form})
    return HttpResponse(content='401 Unauthorized', status=401)

@login_required(login_url='accounts:login')
def article_delete(request, slug):
    article = Article.objects.get(slug=slug)
    if request.user.id == article.author.id:
        if request.method == 'POST':
            article.delete()
            return redirect('homepage')
        return render(request, template_name='articles/article_confirm_delete.html', context={'article': article})
    return HttpResponse(content='401 Unauthorized', status=401)