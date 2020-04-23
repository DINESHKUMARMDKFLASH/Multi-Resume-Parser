from django.shortcuts import render, redirect

from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('index/', views.index,name='index'),
    path('view/', views.view,name='view'),
    path('resume/', views.resume,name='resume'),
    path('addmore/',views.addmore,name='addmore'),
    path('noofres/',views.noofres,name='noofres'),
    path('curview/<int:id>',views.curview,name='curview'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update')
]