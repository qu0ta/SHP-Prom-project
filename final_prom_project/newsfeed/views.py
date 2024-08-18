from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User as BaseUser
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render

from .forms import CommentForm, RegisterUserForm
from .news_services import (create_comment, get_all_news,
                            get_comments_by_news_id, get_last_news, get_news,
                            get_user_by_user_id)


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


def one_news_view(request: WSGIRequest, id: int):

    user = get_user_by_user_id(request.user.id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['text']
            news = get_news(news_id=id)
            create_comment(author=user, news=news, text=comment_text)
            return redirect(f'/news/{id}')
        else:
            errors = form.errors
            print(errors)
            return redirect(f'/news/{id}')

    form = CommentForm()

    comments = get_comments_by_news_id(news_id=id)
    concrete = get_news(news_id=id)
    context = {
        'form': form,
        'comments': comments,
    }

    if not concrete:
        context['error'] = True
        context['message'] = "Новость не найдена"
        page_title = "Такой новости нет"
    else:
        page_title = concrete.title
        context['news'] = concrete
    context['page_title'] = page_title
    context['user'] = user

    return render(request, 'pages/one_news.html', context=context)


def registration_view(request: WSGIRequest):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = BaseUser.objects.create_user(
                username=username, password=password)
            user.save()
            login(request, user)
            return redirect('/')

        errors = form.errors
        print(errors)
        return

    form = RegisterUserForm()

    context = {
        'form': form,
    }

    return render(request, 'pages/registration.html', context=context)


def login_view(request: WSGIRequest):
    pass
