from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.sites.models import Site
from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class Menu(models.Model):
    """Меню"""
    name = models.CharField("Название", max_length=100)
    is_auth = models.BooleanField("Только для залогиненых", default=False)
    active = models.BooleanField("Отображение", default=False)

    def __str__(self):
        return self.name

    def items(self):
        return self.menuitem_set.all()

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class MenuItem(MPTTModel):
    """Пункты меню"""
    name = models.CharField("Название на лат.", max_length=100)
    title = models.CharField("Название пункта на сайте", max_length=100)
    parent = TreeForeignKey(
        'self',
        verbose_name="Род. пункт меню",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey(Menu, verbose_name="Меню", on_delete=models.CASCADE)
    status = models.BooleanField("Отображение", default=False)
    is_auth = models.BooleanField("Только для залогиненых", default=False)
    url = models.CharField("Ссылка на внешний ресурс", max_length=100, null=True, blank=True)
    anchor = models.CharField("Якорь", max_length=255, null=True, blank=True)

    limit = models.Q(app_label="blog", model="post") | \
            models.Q(app_label="blog", model="category") | \
            models.Q(app_label="feedback", model="feedbackmodel") | \
            models.Q(app_label="pages", model="pages")

    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to=limit,
        verbose_name="Ссылка на: ",
        on_delete=models.CASCADE,
        null=True,
        blank=True,)
    object_id = models.PositiveIntegerField(verbose_name='ID записи', default=1, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def get_anchor(self):
        if self.anchor:
            return "{}/#{}".format(Site.objects.get_current().domain, self.anchor)
        else:
            return False

    def __str__(self):
        return self.name

    content_object.short_description = 'ID'

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
