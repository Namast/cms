from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Pages


class PagesAdminForm(forms.ModelForm):
    """Форма с виджетом CKEditor"""
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Pages
        fields = "__all__"


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    """Статичные страницы"""
    list_display = ("title", "published", "id")
    list_editable = ("published",)
    list_filter = ("published", "template")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title", )}
    form = PagesAdminForm