import datetime
from typing import Any

from django.core.handlers.wsgi import WSGIRequest

from .models import News, User, Comment
from django.contrib.auth.models import User as BaseUser


def get_last_news(count: int) -> list[News]:
	return get_all_news()[:count]


def get_all_news() -> list[News]:
	return News.objects.all().order_by('-created_at')


def get_news(news_id: int) -> News | None:
	try:
		return News.objects.get(pk=news_id)
	except News.DoesNotExist:
		return None


def get_user_by_username(username: str) -> User | None:
	try:
		return User.objects.get(username=username)
	except User.DoesNotExist:
		return None


def create_comment(author: User, news: News, text: str, created_at=None) -> None:
	if created_at:
		Comment(author=author, news=news, text=text, created_at=created_at).save()
		return
	Comment(author=author, news=news, text=text).save()


def get_comments_by_news_id(news_id: int) -> list[Comment]:
	return Comment.objects.filter(news=News.objects.get(pk=news_id))


def create_base_user(password: str, username: str) -> BaseUser:
	user = BaseUser.objects.create_user(
		username=username, password=password)
	user.save()
	return user


def create_user(fullname: str, birthdate: datetime.date, email: str, about: str, username: str) -> None:
	User.objects.create(
		fullname=fullname,
		birthday=birthdate,
		email=email,
		about=about,
		username=username
	).save()


def check_auth_to_context(request: WSGIRequest, context: dict) -> dict:
	user = request.user
	auth = True if user.is_authenticated else False
	context['auth'] = auth
	return context


def get_news_by_title(title: str) -> list[News]:
	return News.objects.filter(title__contains=title)


__all__ = [
	'create_comment',
	'get_all_news',
	'get_comments_by_news_id',
	'get_last_news',
	'get_news',
	'get_user_by_username',
	'create_base_user',
	'create_user',
	'check_auth_to_context',
	'get_news_by_title',
]
