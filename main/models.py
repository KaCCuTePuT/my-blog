from pytils.translit import slugify
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField('Заглавие', unique=True, max_length=100)
    slug = models.SlugField()
    text = models.TextField('Содержание')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    date = models.DateTimeField('Дата создания', auto_now_add=True)
    img = models.ImageField('Изображение', null=True, help_text='Ширина изображения должна быть не менее 300 пикселей')
    draft = models.BooleanField('Черновик', default=False)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:post_detail", kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    text = models.TextField('Текст')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE)
    date = models.DateTimeField('Дата добавления', auto_now_add=True)
    active = models.BooleanField('Активен?', default=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



