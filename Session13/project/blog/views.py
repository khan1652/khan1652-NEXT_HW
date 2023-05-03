from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})


@login_required(login_url="accounts:login")
def new(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            title=request.POST["title"],
            content=request.POST["content"],
            author=request.user,
        )
        return redirect("blog:detail", new_post.pk)
    return render(request, "blog/new.html")


@login_required(login_url="accounts:login")
def detail(request, post_pk):
    post = Post.objects.get(id=post_pk)
    if request.method == "POST":
        Comment.objects.create(
            post=post,
            content=request.POST["content"],
            author=request.user,
        )
        return redirect("blog:detail", post_pk)
    return render(request, "blog/detail.html", {"post": post})


@login_required(login_url="accounts:login")
def update(request, post_pk):
    posts = Post.objects.all()
    post = Post.objects.get(id=post_pk)
    if post.author == request.user:
        if request.method == "POST":
            Post.objects.filter(id=post_pk).update(
                title=request.POST["title"],
                content=request.POST["content"],
            )
            return redirect("blog:detail", post_pk)
        return render(request, "blog/update.html", {"post": post})
    else:
        error = "Not authorized"
        return render(request, "blog/home.html", {"posts": posts, "error": error})


@login_required(login_url="accounts:login")
def delete(request, post_pk):
    posts = Post.objects.all()
    post = Post.objects.get(id=post_pk)
    if post.author == request.user:
        post.delete()
        return redirect("blog:home")
    else:
        error = "Not authorized"
        return render(request, "blog/home.html", {"posts": posts, "error": error})


@login_required(login_url="accounts:login")
def deleteComment(request, post_pk, comment_pk):
    posts = Post.objects.all()
    comment = Comment.objects.get(id=comment_pk)
    if comment.author == request.user:
        comment.delete()
        return redirect("blog:detail", post_pk)
    else:
        error = "Not authorized"
        return render(request, "blog/home.html", {"posts": posts, "error": error})
