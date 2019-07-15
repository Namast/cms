from django.db import models
from django.urls import reverse


class Pages(models.Model):
    """Страницы"""
    title = models.CharField("Заголовок", max_length=500)
    text = models.TextField("Текст", blank=True)
    template = models.CharField("Шаблон", max_length=500, default="pages/home.html")
    published = models.BooleanField("Опубликовать?", default=True)
    slug = models.SlugField("URL", max_length=500, default="", null=True, blank=True, help_text="Укажите url", unique=True)
    description = models.TextField("Description", max_length=300, null=True)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.slug:
            return reverse("page", kwargs={"slug": self.slug})
        else:
            return reverse("page")