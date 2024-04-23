from datetime import datetime
import random
from django.shortcuts import redirect, render, HttpResponse

from cars.form import PostForm, ReviewForm
from cars.models import Post

def main_view(request):
    if request.method == 'GET':
        now = datetime.now()
        
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

        context = {
            'current_date_time': formatted_now
        }
        return render(request, 'main.html', context)
    


def hello_view(request):
    if request.method == 'GET':  
        return HttpResponse("Hello! It's my project")


def fun_view(request):
    if request.method == 'GET':
        anecdotes = [
            "Если у вас закончилась мазь от зуда,\n — Не спешите выбрасывать тюбик.\n Его уголком очень удобно чесаться.",
            "Бармен спрашивает пьяного посетителя:\n— Я вижу, у вас пустой стакан. Не хотите ли еще один?\nА на хрена мне два пустых стакана?",
            "Дорогой, ты с чем картошечку будешь на ужин?\n— С мясом.\nЯ как знала и купила чипсы с беконом."
        ]
        anecdote = random.choice(anecdotes)
        return HttpResponse(anecdote) 

def post_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        context = {'posts': posts}
        
        return render (request, 'cars/post_list.html', context)
    
def post_detail_view(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=post_id)
            
        except Post.DoesNotExist:
            return HttpResponse('Post not found', status=404)
        
        context = {'post': post}
        return render (request, 'cars/post_detail.html', context)
    
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render (request, 'cars/post_create.html', {'form': form})
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('post_list_view')
        return render (request, 'cars/post_create.html', {'form': form})
    
    
    
def add_review_view(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.post = post
            review.save()
            return redirect('post_detail_view', post_id=post_id)
    else:
        form = ReviewForm()

    return render(request, 'cars/add_review.html', {'form': form, 'post': post})