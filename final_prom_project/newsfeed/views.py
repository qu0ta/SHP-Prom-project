from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def home_view(request: WSGIRequest):
    request_user = request.user
    if request_user.is_authenticated:
        username = request_user.username
        if not username:
            username = "AnonymousUser"
    else:
        username = "AnonymousUser"

    context = {
        'page_title': 'Главная',
        'username': username,
    }
    return render(request, 'pages/home.html', context)


def about_view(request: WSGIRequest):
    context = {
        'page_title': 'О нас',
    }
    return render(request, 'pages/about.html', context)
