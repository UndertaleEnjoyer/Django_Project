from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import CreateArticle

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
    return render(request, template_name='articles/article_create.html', context={'form': form})