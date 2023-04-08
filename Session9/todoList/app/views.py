from django.shortcuts import render, redirect
from .models import Post
from datetime import datetime

# Create your views here.
def home(request):
    todos=Post.objects.all()
    now=datetime.now()
    sorted=[]
    done=[]

    for todo in todos:
        if(todo.do==False):
            todo.d_day=todo.time.date()-now.date()
            todo.d_day=todo.d_day.days
            if (todo.d_day<0):
                todo.outdated=True
            else:
                todo.outdated=False
            sorted.append(todo)
        else:
            done.append(todo)
    sorted.sort(key=lambda x: x.d_day)
    return render(request, 'home.html', {'todos':sorted, 'done':done})

def new(request):
    if request.method=="POST":
        deadline=request.POST['time']
        deadline=datetime.fromisoformat(deadline)
        new=Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            time=deadline,
        )
        return redirect('detail', new.id)
    return render(request, 'new.html')

def update(request, todo_id):
    todo=Post.objects.get(id=todo_id)
    deadline=datetime.isoformat(todo.time)
    
    if request.method=='POST':
        time=request.POST['time']
        Post.objects.filter(id=todo_id).update(
            title=request.POST['title'],
            content=request.POST['content'],
            time=datetime.fromisoformat(time),
        )
        return redirect('detail', todo_id)

    return render(request, 'update.html', {'todo': todo, 'time':deadline})

def detail(request, todo_id):
    todo=Post.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo':todo})

def delete(request, todo_id):
    todo=Post.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')

def do(request, todo_id):
    Post.objects.filter(id=todo_id).update(
        do=True,
    )
    return redirect('home')