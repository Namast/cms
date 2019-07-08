from django import template

from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/tags/category.html')
def category_list(publish=True):
    """Template Tag вывода категорий"""
    category = Category.objects.filter(active=publish)
    return {"category_list": category}



@register.filter()
def comment_padding(value):
    """Filter сдвига комментария"""
    return int(value / 2) == float(value / 2)

