from .models import Category


def category_list(request):
    """Контекст процессор для категорий"""
    return {"list_category": Category.objects.all()}