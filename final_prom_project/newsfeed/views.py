from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render

from .forms import CommentForm, RegisterUserForm, LoginUserForm
from .news_services import (create_comment, get_all_news,
							get_comments_by_news_id, get_last_news, get_news,
							get_user_by_username, create_base_user, create_user, check_auth_to_context)


def home_view(request: WSGIRequest):
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
	print(context['auth'])
	return render(request, 'pages/home.html', context)


def about_view(request: WSGIRequest):
	context = {
		'page_title': 'О нас',
	}
	context = check_auth_to_context(request, context)
	return render(request, 'pages/about.html', context)


@login_required(login_url='/registration')
def all_news_view(request: WSGIRequest):
	news = get_all_news()
	context = {
		'page_title': 'Все новости',
		'news': news
	}
	context = check_auth_to_context(request, context)
	return render(request, 'pages/all_news.html', context)


@login_required(login_url='/registration')
def one_news_view(request: WSGIRequest, id: int):
	user = get_user_by_username(request.user.username)
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
	context = check_auth_to_context(request, context)

	return render(request, 'pages/one_news.html', context=context)


def registration_view(request: WSGIRequest):
	if request.method == 'POST':
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			birthdate = form.cleaned_data['birthdate']
			fullname = form.cleaned_data['fullname']
			about = form.cleaned_data['about']

			user = create_base_user(password, username)

			create_user(fullname, birthdate, email, about, username)
			login(request, user)
			return redirect('/')

		errors = form.errors
		print(errors)
		return

	form = RegisterUserForm()

	context = {
		'form': form,
	}
	context = check_auth_to_context(request, context)

	return render(request, 'pages/registration.html', context=context)


def login_view(request: WSGIRequest):
	if request.method == 'POST':
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
	user = get_user_by_username(request.user.username)
	print(user)


@login_required(login_url='/registration')
def logout_view(request: WSGIRequest):
	logout(request)
	return redirect('/')
