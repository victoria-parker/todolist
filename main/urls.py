from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('create/', views.create, name="create"),
    path('lists/',views.viewToDoLists,name="viewtodolists"),
    path('lists/<int:id>',views.listItems,name='listitems')
]