from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Модель категорий к статье"""
    name = models.CharField("Название", max_length=150)
    slug = models.SlugField("url", max_length=160)
    published = models.BooleanField("Опубликовать", default=True)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    """Модель тегов к статье"""
    name = models.CharField("Название", max_length=50)
    slug = models.SlugField("url", max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    """Модель статей"""
    title = models.CharField("Заголовок", max_length=150)
    description = models.TextField("Превью статьи", max_length=500)
    text = models.TextField("Статья")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    publish_data = models.DateTimeField("Дата публикации", default=timezone.now)
    published = models.BooleanField("Опубликовать", default=True)
    sort = models.PositiveIntegerField("Порядок", default=0, unique=True)
    view = models.PositiveIntegerField("Просмотры", default=0)
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    slug = models.SlugField("url", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created"]


class CommentPost(models.Model):
    """Комментарии к статье"""
    post = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE)
    text = models.TextField("Комментарий", max_length=1000)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    moderation = models.BooleanField("Опубликовать", default=False)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
