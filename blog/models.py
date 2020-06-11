from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from tinymce import models as tinymce_models


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'В разработке'),
        ('published', 'Опубликована'),
    )

    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='Слаг')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    annotation = models.TextField(max_length=300, default='', verbose_name='Текст превью')
    body = tinymce_models.HTMLField(verbose_name='Текст')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Время публикации')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])

    def has_like(self, user):
        return self.likes.filter(author=user).first()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Статья')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments', default=None,
                               verbose_name='Автор')
    body = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    active = models.BooleanField(default=True, verbose_name='Статус активности')

    class Meta:
        ordering = ('created',)
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return 'Comment by {} on {}'.format(self.body, self.post)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', verbose_name='Статья')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_likes', default=None,  verbose_name='Автор')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return 'Like by {} from {}'.format(self.post, self.author)


class Property(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Слаг')
    body = tinymce_models.HTMLField(verbose_name='Текст')

    objects = models.Manager()

    class Meta:
        verbose_name = 'CSS свойство'
        verbose_name_plural = 'CSS свойства'

    def __str__(self):
        return 'Property {}'.format(self.title)

    def first_letter(self):
        return self.title[0]
