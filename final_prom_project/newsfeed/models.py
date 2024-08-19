"""Модели для приложения newsfeed."""
from django.db import models


def _author_directory_path(instance, filename):
    """Функция для создания пути к изображению.
    
    :param instance: экземпляр модели
    :param filename: имя файла

    :return: путь к изображению
    """
    return "user_{0}/image_{1}".format(instance.author.id,  filename)


class User(models.Model):
    """Модель пользователя."""
    username = models.CharField(max_length=100, default='DEFAULT USERNAME')
    fullname = models.CharField(max_length=30, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    about = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):

        return self.fullname


class News(models.Model):
    """Модель новостей."""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=_author_directory_path)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100, verbose_name='desc')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.image.url}"

class Comment(models.Model):
    """Модель комментариев."""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment: {self.text}"