from datetime import date
from django.core.validators import MaxValueValidator
from django.db import models


class Category(models.Model):
    """Модель для категорий"""
    name = models.CharField(max_length=30,
                            verbose_name='Название категории')

    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель для жанров"""
    name = models.CharField(max_length=30,
                            verbose_name='Название жанра')

    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель для произведений"""
    name = models.CharField(max_length=50,
                            verbose_name='Название произведения')

    year = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(date.today().year,
                                      message='дружище, ты ошибся годом'
                                      ),
                    ],
    )

    description = models.TextField(
        blank=True,
        max_length=200,
        verbose_name='описание')

    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='titles',
        verbose_name='жанр')

    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='категория')


    class Meta:
        ordering = ('year',)
        verbose_name = 'Произведение'

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    """я не знаю что тут делать"""
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
