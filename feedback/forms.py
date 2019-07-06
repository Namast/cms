from django.forms import ModelForm
from .models import FeedbackModel


class FeedbackForm(ModelForm):
    """Форма обратной связи"""
    class Meta:
        model = FeedbackModel
        exclude = ['date']