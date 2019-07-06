from django.contrib import admin

from .models import FeedbackModel


@admin.register(FeedbackModel)
class FeedbackModel(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['name', 'email', 'phone', 'message']