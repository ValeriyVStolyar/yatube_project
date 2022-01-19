from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком соц групп
def group_posts(request, slug):
    return HttpResponse('Список социальных групп')


def group_posts(request, sl, n, str):
    return HttpResponse('Slug/Number/String')