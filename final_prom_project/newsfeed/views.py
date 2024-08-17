from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import News


def home_view(request: WSGIRequest):
    request_user = request.user
    if request_user.is_authenticated:
        username = request_user.username
        if not username:
            username = "AnonymousUser"
    else:
        username = "AnonymousUser"

    last_news = _get_last_news(3)
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


def _get_last_news(count: int) -> list[News]:
    return News.objects.all().order_by('-created_at')[:count]
