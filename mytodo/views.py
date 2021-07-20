from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from .models import *
from .forms import TaskForm
def index(request):
    task=Task.objects.all()
    form=TaskForm()
    
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            print("Asd,as")
            return redirect('/')
    context={"task":task,"form":form}
    return render(request,'mytodo/index.html',context)
def update_tod(request,pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    print("yeahhhh")
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        print("yesssss")
        if form.is_valid():
            form.save()
            return redirect("/")
    context={"form":form}
    return render(request,'mytodo/update_todo.html',context)

def delete_todo(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect("/")
