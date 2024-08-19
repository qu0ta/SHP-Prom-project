"""
This module contains views for the newsfeed application.

.. module:: newsfeed.views
   :synopsis: Contains views for the newsfeed application.

.. moduleauthor:: Stanislaw Gupaliuk

"""
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render

from .forms import CommentForm, RegisterUserForm, LoginUserForm
from .news_services import *


def home_view(request: WSGIRequest):
	"""
	Обработчик запроса на главную страницу

	:param request: Объект запроса
	:return: Объект ответа
	"""
	if request.method == 'POST':
		if title := request.POST.get('news_search', None):
			news = get_news_by_title(title)
			context = {
				'news': news,
				'page_title': 'Главная',
				'username': request.user.username,
			}
			return render(request, 'pages/all_news.html', context=context)
	request_user = request.user
	if request_user.is_authenticated:
		username = request_user.username
		if not username:
			username = "AnonymousUser"
	else:
		username = "AnonymousUser"

	last_news = get_last_news(count=3)
	context = {
		'page_title': 'Главная',
		'username': username,
		'news': last_news,
	}
	context = check_auth_to_context(request, context)
	return render(request, 'pages/home.html', context)


def about_view(request: WSGIRequest):
	"""
	Обработчик запроса на страницу "О нас"

	:param request: Объект запроса
	:return: Объект ответа
	"""
	if request.method == 'POST':
		if title := request.POST.get('news_search', None):
			news = get_news_by_title(title)
			context = {
				'news': news,
				'page_title': 'Главная',
				'username': request.user.username,
			}
			return render(request, 'pages/all_news.html', context=context)
	context = {
		'page_title': 'О нас',
	}
	context = check_auth_to_context(request, context)
	return render(request, 'pages/about.html', context)


@login_required(login_url='/registration')
def all_news_view(request: WSGIRequest):
	"""
	Обработчик запроса на страницу "Все новости"
	Требует авторизацию

	:param request: Объект запроса
	:return: Объект ответа
	"""
	if request.method == 'POST':
		if title := request.POST.get('news_search', None):
			news = get_news_by_title(title)
			context = {
				'news': news,
				'page_title': 'Главная',
				'username': request.user.username,
			}
			return render(request, 'pages/all_news.html', context=context)
	news = get_all_news()
	context = {
		'page_title': 'Все новости',
		'news': news
	}
	context = check_auth_to_context(request, context)
	return render(request, 'pages/all_news.html', context)


@login_required(login_url='/registration')
def one_news_view(request: WSGIRequest, id: int):
	"""
	Обработчик запроса на страницу одной новости.
	Требует авторизацию

	:param request: Объект запроса
	:param id: Идентификатор новости
	:return: Объект ответа
	"""
	user = get_user_by_username(request.user.username)
	if not user:
		create_user(username=request.user.username)
		user = get_user_by_username(request.user.username)

	if request.method == 'POST':
		if title := request.POST.get('news_search', None):
			news = get_news_by_title(title)
			context = {
				'news': news,
				'page_title': 'Главная',
				'username': request.user.username,
			}
			return render(request, 'pages/all_news.html', context=context)
		form = CommentForm(request.POST)
		if form.is_valid():
			comment_text = form.cleaned_data['text']
			news = get_news(news_id=id)
			if news:
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
	context = check_auth_to_context(request, context)

	return render(request, 'pages/one_news.html', context=context)


def registration_view(request: WSGIRequest):
	"""
	Обработчик запроса на страницу "Регистрация"

	:param request: Объект запроса
	:return: Объект ответа
	"""
	if request.method == 'POST':
		if title := request.POST.get('news_search', None):
			news = get_news_by_title(title)
			context = {
				'news': news,
				'page_title': 'Главная',
				'username': request.user.username,
			}
			return render(request, 'pages/all_news.html', context=context)
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			birthdate = form.cleaned_data['birthdate']
			fullname = form.cleaned_data['fullname']
			about = form.cleaned_data['about']

			user = create_base_user(password, username)

			create_user(username=username, birthdate=birthdate, fullname=fullname, about=about, email=email)
			login(request, user)
			return redirect('/')

		errors = form.errors
		context = {
			'form': form,
			'errors': errors,
			'page_title': 'Регистрация'
		}
		return render(request, 'pages/registration.html', context=context)

	form = RegisterUserForm()

	context = {
		'form': form,
		'page_title': 'Регистрация'
	}
	context = check_auth_to_context(request, context)

	return render(request, 'pages/registration.html', context=context)


def login_view(request: WSGIRequest):
	"""
	Обработчик запроса на страницу "Вход"
	:param request: Объект запроса
	:return: Объект ответа
	"""
	if request.method == 'POST':
		if title := request.POST.get('news_search', None):
			news = get_news_by_title(title)
			context = {
				'news': news,
				'page_title': 'Главная',
				'username': request.user.username,
			}
			return render(request, 'pages/all_news.html', context=context)
		form = LoginUserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			if user := authenticate(request, username=username, password=password):
				login(request, user)
				return redirect('/')

	form = LoginUserForm()

	context = {
		'form': form,
	}
	context = check_auth_to_context(request, context)
	return render(request, 'pages/login.html', context=context)


@login_required(login_url='/registration')
def profile_view(request: WSGIRequest):
	"""
	Обработчик запроса на страницу "Профиль"
	Требует Авторизацию

	
	:param request: Объект запроса
	:return: Объект ответа
	"""
	if request.method == 'POST':
		if title := request.POST.get('news_search', None):
			news = get_news_by_title(title)
			context = {
				'news': news,
				'page_title': 'Главная',
				'username': request.user.username,
			}
			return render(request, 'pages/all_news.html', context=context)
	user = get_user_by_username(request.user.username)
	context = {'user': user,
			'page_title': 'Профиль'}
	context = check_auth_to_context(request, context)
	return render(request, 'pages/profile.html', context)


@login_required(login_url='/registration')
def logout_view(request: WSGIRequest):
	"""
	Обработчик запроса на страницу "Выход"
	Требует Авторизацию
	:param request: Объект запроса
	:return: Объект ответа
	"""
	logout(request)
	return redirect('/')
