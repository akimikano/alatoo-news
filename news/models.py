from datetime import datetime

from django.db import models
from users.models import Account


class NewsItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Оглавление')
    content = models.TextField(verbose_name='Текст')
    image = models.ImageField(verbose_name='Изображение', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Автор комментария')
    news = models.ForeignKey(NewsItem, on_delete=models.CASCADE, verbose_name='Новость')
    content = models.TextField(verbose_name='Комментарий')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.name_surname

