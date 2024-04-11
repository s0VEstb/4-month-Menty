from datetime import datetime
import random
from django.shortcuts import render, HttpResponse

def main_view(request):
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
    anecdotes = [
        "Если у вас закончилась мазь от зуда,\n — Не спешите выбрасывать тюбик.\n Его уголком очень удобно чесаться.",
        "Бармен спрашивает пьяного посетителя:\n— Я вижу, у вас пустой стакан. Не хотите ли еще один?\nА на хрена мне два пустых стакана?",
        "Дорогой, ты с чем картошечку будешь на ужин?\n— С мясом.\nЯ как знала и купила чипсы с беконом."
    ]
    anecdote = random.choice(anecdotes)
    return HttpResponse(anecdote)
