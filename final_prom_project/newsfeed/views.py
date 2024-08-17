from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .news_services import get_last_news, get_all_news


def home_view(request: WSGIRequest):
    request_user = request.user
    if request_user.is_authenticated:
        username = request_user.username
        if not username:
            username = "AnonymousUser"
    else:
        username = "AnonymousUser"

    last_news = get_last_news(count=3)
    for n in last_news:
        print(n.image.url, 'helllllo')
    context = {
        'page_title': 'Главная',
        'username': username,
        'news': last_news,
    }
    return render(request, 'pages/home.html', context)


def about_view(request: WSGIRequest):
    context = {
        'page_title': 'О нас',
    }
    return render(request, 'pages/about.html', context)


def all_news_view(request: WSGIRequest):
    news = get_all_news()
    context = {
        'page_title': 'Все новости',
        'news': news
    }
    return render(request, 'pages/all_news.html', context)
