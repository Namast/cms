from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Post, Tag, Category, Comment


class CategoryAdmin(MPTTModelAdmin):
    """Категории"""
    mptt_level_indent = 20


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Статьи"""
    list_display = ("id", "title", "created", "publish_date", "active", "sort", "view", "category")
    list_display_links = ("title",)
    list_filter = ("category", "created")
    list_editable = ("sort", "active")
    search_fields = ("title",)
    inlines = [CommentInline]
    readonly_fields = ("view",)
    # fields = ("title", "text")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'parent')
    list_filter = ('active',)
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ('active',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'moderated',)
    list_editable = ('moderated',)


# admin.site.register(Post, PostAdmin)
# admin.site.register(Tag)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Comment)