from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewList
from .models import ToDoList, Item
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    return render(request, "main/index.html",{})

def create(request):
      if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList.objects.create(name=n, user=request.user)
        return redirect("viewtodolists")
      
      else:      
        form = CreateNewList()
      return render(request, "main/create.html",{"form":form} )

def viewToDoLists(request):
    l = ToDoList.objects.all()
    return render(request, "main/lists.html",{"lists":l} )

def listItems(request,id):
    todolist = ToDoList.objects.get(id=id)

    if request.method == 'POST':

        # * FOR NEW ITEMS
        if 'newItem' in request.POST and len(request.POST.get('new')) is not 0:
            item_txt = request.POST.get('new')
            Item.objects.create(todoList=todolist, text=item_txt, complete=False)

        # * FOR UPDATING ITEMS
        if 'save' in request.POST:
            print(request.POST)
            for item in todolist.items.all():
                # updates check
                if request.POST.get(str(item.id)) == 'checked':
                    item.complete = True
                else:
                    item.complete = False
                #updates text
                item.text = request.POST.get('item_'+str(item.id)+'_txt')

                item.save()

        return redirect('listitems', id=id)
    else:
        items = todolist.items.all().order_by('-id')
        return render(request,'main/list.html',{'list': todolist, 'items': items})

def deleteItem(request,item_id,list_id):
        item = get_object_or_404(Item, pk=item_id, todoList_id=list_id)
        item.delete()
        return redirect('listitems', id=list_id)

def deleteList(request,id):
        todo_list = get_object_or_404(ToDoList, pk=id)
        todo_list.delete()
        return redirect("viewtodolists")

def editList(request,id):
        todolist = get_object_or_404(ToDoList, pk=id)
        # * FOR UPDATING ITEMS
        if 'save' in request.POST:
            #updates name
            todolist.name = request.POST.get('todolist_name')
            todolist.save()
            return redirect('viewtodolists')

        return render(request,'main/edit.html',{'list': todolist})

        


