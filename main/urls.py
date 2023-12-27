from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('create/', views.create, name="create"),
    path('lists/',views.viewToDoLists,name="viewtodolists"),
    path('lists/<int:id>',views.listItems,name='listitems'),
    path('todolist/<int:list_id>/deleteitem/<int:item_id>/', views.deleteItem, name='deleteItem'),
    path('deletelist/<int:id>/', views.deleteList, name='deleteList'),
    path('editlist/<int:id>/', views.editList, name='editList'),
]