from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком соц групп
    path('group/<slug:slug>/', views.group_posts),
    path('group/<slug:sl>/<int:n>/<str>', views.group_posts),
]
