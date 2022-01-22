from django.shortcuts import render
# Импортируем модель, чтобы обратиться к ней
from .models import Post

# Create your views here.
# from django.http import HttpResponse


# Главная страница
# def index(request):
    # return HttpResponse('Главная страница')


def index(request):
    # template = 'ice_cream/index.html'
    # template = 'posts/templates/index.html'
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
    }
    return render(request, template, context)


def index(request):
    template = 'posts/index.html'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Это главная страница проекта Yatube'
    # Словарь с данными принято называть context
    # В словаре context отправляем информацию в шаблон
    context = {
        # В словарь можно передать переменную
        'title': title,
        'posts': posts,
    }
    # return render(request, 'posts/index.html', context)
    return render(request, template, context)


# Страница со списком соц групп
# def group_posts(request, slug):
    # return HttpResponse('Список социальных групп')


# def group_posts(request, slug):
def group_posts(request):
    template_groups = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    # slug = 'slug'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # 'slug': slug,
    }
    return render(request, template_groups, context)


# def group_posts(request, sl, n, str):
#     return HttpResponse('Slug/Number/String'
#     '<br>Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
#         'если у тебя нет правильных <s>вопросов</s> запросов.</b>')
