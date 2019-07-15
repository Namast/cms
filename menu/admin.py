from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Menu, MenuItem


@admin.register(Menu)
class Menu(admin.ModelAdmin):
    """Меню"""
    list_display = ("id", "name", "is_auth", "active")
    list_editable = ("is_auth", "active")
    list_display_links = ("name",)


@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):
    """Пункты меню"""
    mptt_level_indent = 20
    list_display = ("id", "name", "title", "menu", "status", "is_auth")
    list_editable = ("title", "menu", "status", "is_auth")
    list_display_links = ("name",)