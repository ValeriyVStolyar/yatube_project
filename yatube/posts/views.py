from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Group, Post

# Create your views here.
# from django.http import HttpResponse


# Главная страница
# def index(request):
    # return HttpResponse('Главная страница')


def index(request):
    # template = 'ice_cream/index.html'
    # template = 'posts/templates/index.html'
    template = 'posts/index.html'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # title = 'Это главная страница проекта Yatube'
    # Словарь с данными принято называть context
    # В словаре context отправляем информацию в шаблон
    context = {
        # В словарь можно передать переменную
        # 'title': title,
        'posts': posts,
    }
    # return render(request, 'posts/index.html', context)
    return render(request, template, context)


# Страница со списком соц групп
# def group_posts(request, slug):
    # return HttpResponse('Список социальных групп')


def group_posts(request, slug):
# def group_posts(request):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    template_groups = 'posts/group_list.html'
    # title = 'Здесь будет информация о группах проекта Yatube'
    # slug = 'slug'
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        # 'title': title,
        'group': group,
        'posts': posts,
        # 'slug': slug,
    }
    return render(request, template_groups, context)
    # return render(request, 'posts/group_list.html', context)


# def group_posts(request, sl, n, str):
#     return HttpResponse('Slug/Number/String'
#     '<br>Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
#         'если у тебя нет правильных <s>вопросов</s> запросов.</b>')
