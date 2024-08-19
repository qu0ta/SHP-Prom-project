"""
Модуль содержит всю бизнес-логику приложения.

.. module:: news_services
   :synopsis: Функции, реализующие бизнес-логику приложения.

.. moduleauthor:: Stanislaw Gupaliuk
"""
import datetime
from django.core.handlers.wsgi import WSGIRequest

from .models import News, User, Comment
from django.contrib.auth.models import User as BaseUser


def get_last_news(count: int) -> list[News]:
	"""
	Получить последние новости.
	:param count: Количество новостей.
	:type count: int
	:return: Список новостей.
	:rtype: list[News]
	"""
	return get_all_news()[:count]


def get_all_news() -> list[News]:
	"""
		Получить все новости.
		:return: Список всех новостей.
		:rtype: list[News]
	"""
	return News.objects.all().order_by('-created_at')


def get_news(news_id: int) -> News:
	"""
		Получить новость по ID.
		:param news_id: ID новости.
		:type news_id: int
		:return: Новость с указанным ID.
		:rtype: News
	"""

	try:
		return News.objects.get(pk=news_id)
	except News.DoesNotExist:
		return None
	
def get_news_by_title(title: str) -> list[News]:
	"""
    Получить новости по названию.
    :param title: Название новости.
    :type title: str
    :return: Список новостей с совпадающим названием.
    :rtype: list[News]
    """
	return News.objects.filter(title__contains=title)


def get_user_by_username(username: str) -> User:
	"""
		Получить пользователя по имени.
		:param username: Имя пользователя.
		:type username: str
		:return: Пользователь с указанным именем.
		:rtype: User
	"""

	try:
		return User.objects.get(username=username)
	except User.DoesNotExist:
		return None


def create_comment(author: User, news: News, text: str, created_at=None) -> None:
	"""
    Создать комментарий к новости.
    :param author: Автор комментария.
    :type author: User
    :param news: Новость, к которой относится комментарий.
    :type news: News
    :param text: Текст комментария.
    :type text: str
    :param created_at: Дата и время создания комментария.
    :type created_at: datetime
    """
	if created_at:
		Comment(author=author, news=news, text=text, created_at=created_at).save()
		return
	Comment(author=author, news=news, text=text).save()


def get_comments_by_news_id(news_id: int) -> list[Comment]:
	"""
    Получить комментарии к новости.
    :param news_id: Идентификатор новости.
    :type news_id: int
    :return: Список комментариев к новости.
    :rtype: list[Comment]
    """
	try:
		return Comment.objects.filter(news=News.objects.get(pk=news_id))
	except News.DoesNotExist:
		return []

def create_base_user(password: str, username: str) -> BaseUser:
	"""
	Создание базового пользователя
	:param password: Пароль пользователя
	:type password: str
	:param username: Имя пользователя
	:type username: str
	:return: Объект пользователя
	:rtype: BaseUser
	"""
	user = BaseUser.objects.create_user(
		username=username, password=password)
	user.save()
	return user


def create_user(username: str, fullname: str = None, birthdate: datetime.date = None, email: str = None, about: str = None, ) -> None:
	"""
	Создание нового пользователя
	:param username: Имя пользователя
	:type username: str
	:param fullname: Полное имя пользователя
	:type fullname: str
	:param birthdate: Дата рождения пользователя
	:type birthdate: datetime.date
	:param email: Электронная почта пользователя
	:type email: str
	"""
	User.objects.create(
		fullname=fullname,
		birthday=birthdate,
		email=email,
		about=about,
		username=username
	).save()


def check_auth_to_context(request: WSGIRequest, context: dict) -> dict:
	"""
	Добавление в словарь context поля auth
	:param request: Объект запроса
	:type request: WSGIRequest
	:param context: Словарь с данными
	:type context: dict
	:return: Словарь с данными
	:rtype: dict
	"""
	user = request.user
	auth = True if user.is_authenticated else False
	context['auth'] = auth
	return context


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
