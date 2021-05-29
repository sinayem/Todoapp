from django.shortcuts import render
from .models import Todolist
# Create your views here.
def index(request):
    todo_item = Todolist.objects.order_by('id')
    contex = {"task":todo_item}
    return render(request,'todolist\index.html',contex)