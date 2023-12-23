from django.shortcuts import render, redirect
from .forms import CreateNewList
from .models import ToDoList, Item
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
        return render(request,'main/list.html',{'list': todolist})
