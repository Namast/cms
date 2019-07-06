from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from .forms import FeedbackForm


class FeedbackView(View):
    """Форма обратной связи"""
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback/feedback.html', {'form':form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, settings.MESSAGE_LEVEL, 'Ваше сообщение отправлено')
        else:
            messages.add_message(request, settings.MESSAGE_LEVEL, 'Ошибка')
        return redirect(request.path)

