from django.db import models
from django.urls import reverse


class FeedbackModel(models.Model):
    """Обратная связь"""
    name = models.CharField('ФИО', max_length=100)
    email = models.EmailField('E-mail', max_length=150)
    phone = models.CharField('Телефон', max_length=14, blank=True)
    message = models.TextField('Сообение', max_length=1000)
    date = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("feedback")

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'