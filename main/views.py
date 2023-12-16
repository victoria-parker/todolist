from django.shortcuts import render
from .forms import CreateNewList
from .models import ToDoList
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "main/index.html",{})

def create(request):
      if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList.objects.create(name=n, user=request.user)
        return HttpResponseRedirect("/")
      
      else:      
        form = CreateNewList()
      return render(request, "main/create.html",{"form":form} )

def viewToDoLists(request):
    l = ToDoList.objects.all()
    return render(request, "main/viewtodolists.html",{"lists":l} )
