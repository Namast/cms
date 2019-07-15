from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView

from .models import FeedbackModel
from .forms import FeedbackForm


class FeedbackView(CreateView):
    """Форма обратной связи"""
    model = FeedbackModel
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, settings.MESSAGE_LEVEL, 'Ваше сообщение отправлено')
        return super().form_valid(form)


# class FeedbackView(View):
#     """Форма обратной связи"""
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', {'form':form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, settings.MESSAGE_LEVEL, 'Ваше сообщение отправлено')
#         else:
#             messages.add_message(request, settings.MESSAGE_LEVEL, 'Ошибка')
#         return redirect(request.path)

