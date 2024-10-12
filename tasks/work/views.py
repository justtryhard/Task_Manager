from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from .models import WorkTask
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from .forms import CommentForm


@login_required
def work_home(request):
    worktasks = WorkTask.objects.order_by('type')
    return render(request, 'work/work_home.html', {'worktasks': worktasks})


@login_required
def work_closed(request):
    worktasks_cl = WorkTask.objects.order_by('type')
    return render(request, 'work/work_closed.html', {'worktasks_cl': worktasks_cl})


class CommentMixin:         #класс, позволяющий получить доступ к сущности WorkTask для установления связи с Comments
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):  #включение данных в качестве GET параметров в URL-адрес успеха
        return '%s?id=%s' % (self.success_url, self.object.id)


class WorktaskDetailView(CommentMixin, FormMixin, DetailView):
    model = WorkTask
    template_name = 'work/descr_view.html'
    context_object_name = 'taska'
    form_class = CommentForm
    success_msg = 'Комментарий добавлен'

    def get_success_url(self, **kwargs):
        return reverse_lazy('task-descr', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.worktask = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
