from django.db import models
from django.urls import reverse

from django.utils import timezone


class Quote(models.Model):
    text = models.TextField(verbose_name="Текст", max_length=1024, help_text="Введите текст цитаты")
    date = models.DateTimeField(verbose_name="Дата", db_index=True, default=timezone.now)
    rating = models.IntegerField(verbose_name="Рейтинг", default=0)
    author = models.CharField(verbose_name="Автор", max_length=64, help_text="Введите автора цитаты", blank=True)
    isApproved = models.BooleanField(verbose_name="Утверждена?", default=False)
    isHided = models.BooleanField(verbose_name="Скрыта?", default=False)
    copyPasteRating = models.IntegerField(verbose_name="Рейтинг баянистости", default=0)

    def __str__(self):
        return "#" + str(self.id)

    def get_absolute_url(self):
        return reverse('quote-detail', args=[str(self.id)])

    class Meta:
        ordering = ["id"]


class Comment(models.Model):
    quote = models.ForeignKey('Quote', verbose_name="Цитата", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст", max_length=1000, help_text="Введите текст комментария")
    date = models.DateTimeField(verbose_name="Дата", help_text="Введите дату комментария", default=timezone.now)
    author = models.CharField(verbose_name="Автор", max_length=64, help_text="Введите автора комментария")

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])

    class Meta:
        order_with_respect_to = "quote"

