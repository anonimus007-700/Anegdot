from django.shortcuts import render
from .models import Anecdote

def index(request):
    anecdot_list = Anecdote.objects.all()
    return render(request, 'anecdote/list.html', {'anecdot_list': anecdot_list})
