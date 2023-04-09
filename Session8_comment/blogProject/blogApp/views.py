from django.shortcuts import render, redirect
from .models import Article, Comment, Recomment

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

def home(request):
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

    return render(request, 'home.html', {'articles': articles, 'list': list})

def detail(request, article_id):
    article=Article.objects.get(id=article_id)
    if request.method=="POST":
        Comment.objects.create(
            article=article,
            content=request.POST['content'],
        )
        return redirect('detail', article_id)
    return render(request, 'detail.html', {'article':article})

def category(request, category):
    articles=Article.objects.filter(category=category)
    return render(request, 'category.html', {'articles': articles, 'category': category})

def edit(request, article_id):
    # 카테고리 리스트 확인
    articles = Article.objects.all()
    categories=[]
    for article in articles:
        if article.category not in categories:
            categories.append(article.category)

    article=Article.objects.get(id=article_id)
    if request.method=='POST':
        Article.objects.update(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category'],
        )
        return redirect('detail', article_id)
    return render(request, 'edit.html', {'article':article, 'categories': categories})

def delete(request, article_id):
    article=Article.objects.get(id=article_id).delete()
    return redirect('home')

def deleteComment(request, article_id, comment_id):
    Comment.objects.get(id=comment_id).delete()
    return redirect('detail', article_id)

def recomment(request, article_id, comment_id):
    comment=Comment.objects.get(id=comment_id)
    if request.method=="POST":
        Recomment.objects.create(
            comment=comment,
            content=request.POST['content'],
        )
        return redirect('detail', article_id)

def deleteRecomment(request, article_id, recomment_id):
    Recomment.objects.get(id=recomment_id).delete()
    return redirect('detail', article_id)