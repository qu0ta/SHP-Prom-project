from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def home_view(request: WSGIRequest):
    context = {
        'page_title': 'Главная',
        'username': 'TEST USERNAME',
    }
    return render(request, 'pages/home.html', context)


def about_view(request: WSGIRequest):
    context = {
        'page_title': 'О нас',
    }
    return render(request, 'pages/about.html', context)
