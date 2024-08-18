from django.db import models
from django.conf import settings
import random


def _author_directory_path(instance, filename):
    return "user_{0}/image_{1}.{2}".format(instance.author.id,  random.randint(1, 10000000),
                                           filename.split('.')[-1])


class User(models.Model):
    username = models.CharField(max_length=100, default='DEFAULT USERNAME')
    fullname = models.CharField(max_length=30)
    birthday = models.DateField()
    email = models.EmailField()
    about = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=_author_directory_path)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100, verbose_name='desc')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.image.url}"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment: {self.text}"