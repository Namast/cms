from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/tags/menu-item-tag.html', takes_context=True)
def menu(context, get_menu):
    return {
        "items": MenuItem.objects.filter(
            menu__name=get_menu,
            parent__isnull=True
        ),
    }

