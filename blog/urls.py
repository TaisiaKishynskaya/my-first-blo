from django.urls import path
from . import views

"""Этот шаблон URL-адреса будет соответствовать пустой строке, и преобразователь URL-адресов Django 
    будет игнорировать доменное имя (например, http://127.0.0.1:8000/ ), которое предшествует полному пути URL-адреса. 
    Этот шаблон сообщит Django, что views.post_list это правильное место, если кто-то войдет на ваш сайт по адресу « http://127.0.0.1:8000/ »."""
urlpatterns = [
    path('', views.post_list, name='post_list'),  # присваиваем view call post_listкорневому URL-адресу.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
