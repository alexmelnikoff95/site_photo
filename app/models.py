from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class PhotoDescription(models.Model):
    title = models.CharField(verbose_name='название', max_length=100)
    slug = models.SlugField(unique=True, verbose_name='слаг для фото')
    text = models.TextField(verbose_name='текст')
    data = models.DateField(verbose_name='дата создания', auto_now_add=True)
    image = models.ImageField(verbose_name='изображение', upload_to='photo/description')
    publication = models.BooleanField(verbose_name='опубликовать', default=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-data']
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'


class PhotoCollection(models.Model):
    photo_model = models.ForeignKey(PhotoDescription, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='изображение', upload_to='photo/collection')

    def __str__(self):
        return 'изображение'

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='cлаг')
    text = models.TextField(verbose_name='описание нас')
    image = models.ImageField(verbose_name='изображение', upload_to='photo/about')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Про меня'
        verbose_name_plural = 'Про нас'


class Connection(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    text = models.TextField('сообщение', max_length=5000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
