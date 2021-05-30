from django import forms
from django.db import reset_queries
from django.shortcuts import render,redirect
from .models import Todolist

from .forms import Todolist_form
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
    todo_item = Todolist.objects.order_by('id')
    form = Todolist_form()
    contex = {"task":todo_item,'w':form}
    return render(request,'todolist\index.html',contex)

@require_POST
def add_item(request):
    work = Todolist_form(request.POST)
    #print(request.POST['text'])
    if work.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()
    return redirect('ind')

def completed_todo(request,td_id):
    todo = Todolist.objects.get(pk= td_id)
    todo.completed = True
    todo.save()
    return redirect('ind')

def del_com(request):
    Todolist.objects.filter(completed__exact=True).delete()
    return redirect('ind')

def del_all(request):
    Todolist.objects.all().delete()
    return redirect('ind')