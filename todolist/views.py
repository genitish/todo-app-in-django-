from django.shortcuts import render
from .forms import *
from .models import *
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse ,JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
def home(request):

    list=Todo.objects.all().order_by('-id')
    form = TodoForm()
    if request.method=="POST":
        form=TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
    #if request.method=="POST":
    #    content=request.POST.get('content')
    #    a=Todo(content=content)
    #    a.save()

    return render(request,'todolist/index.html',{'list':list,'form':form})
def see(request,pk):
    list=Todo.objects.filter(pk=pk)

    return render(request,'todolist/schedule.html',{'list':list})

def mark(request,pk):
    todo=Todo.objects.get(pk=pk)
    todo.mark=True
    todo.save()
    return redirect('todolist:home')
def unmark(request,pk):
    todo=Todo.objects.get(pk=pk)
    todo.mark=False
    todo.save()
    return redirect('todolist:home')

def deletecompleted(request):
    Todo.objects.filter(mark__exact=True).delete()

    return redirect('todolist:home')

def delete(request,pk):

    todo=Todo.objects.get(pk=pk)
    todo.delete()

    return redirect('todolist:home')

def update(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
    form = TodoForm()
    if request.method=="POST":
        form=TodoForm(request.POST or None,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todolist:home')
    return render(request,'todolist/update.html',{'form':form})
