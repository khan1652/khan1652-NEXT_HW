from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    # 카테고리 리스트 확인
    articles = Article.objects.all()
    categories=[]
    for article in articles:
        if article.category not in categories:
            categories.append(article.category)


    if request.method=='POST':
        print(request.POST)
        new_article=Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category'],
        )
        return redirect('list')

    return render(request, 'new.html', {'categories':categories})

def list(request):
    # 카테고리 리스트 확인
    articles = Article.objects.all()
    categories=[]
    for article in articles:
        if article.category not in categories:
            categories.append(article.category)

    num=[]
    for category in categories:
        category_articles=Article.objects.filter(category=category)
        num.append(len(category_articles))

    list=zip(categories, num)

    return render(request, 'list.html', {'articles': articles, 'list': list})

def detail(request, article_id):
    article=Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article':article})

def category(request, category):
    articles=Article.objects.filter(category=category)
    return render(request, 'category.html', {'articles': articles, 'category': category})