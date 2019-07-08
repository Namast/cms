from django import template

from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/tags/category.html')
def category_list(publish=True):
    category = Category.objects.filter(active=publish)
    return {"category_list": category}



