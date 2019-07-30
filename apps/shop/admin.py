from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product


class CategoryMPTTModelAdmin(MPTTModelAdmin):
    """Категории"""
    mptt_level_indent = 20


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Product)
