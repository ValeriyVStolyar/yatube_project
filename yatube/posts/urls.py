from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    # path('', views.index),
    path('', views.index, name='main'),
    # Страница со списком соц групп
     #path('group/<slug:slug>/', views.group_posts),
    # path('group/<slug:slug>/', views.group_posts),
    # path('group/', views.group_posts),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    # path('group/', views.group_posts, name='group_list'),
    # path('group/<slug:sl>/<int:n>/<str>', views.group_posts),
]
