from django.urls import path

from . import views

urlpatterns = [


    path('', views.home, name="home"),
    path('read/', views.view_read, name='view_read'),
    path('create/', views.view_create, name='view_create'),
    path('update/<int:id>/', views.view_update, name='view_update'),  # id'yi ekledik
    path('delete/<int:id>/', views.view_delete, name='view_delete'),  # id'yi ekledik
    path('list/', views.view_list, name='todo_list'),
    path('add/', views.todo_add, name='todo_add'),





    
]
