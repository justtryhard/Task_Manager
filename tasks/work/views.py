from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import WorkTask
from django.views.generic import DetailView


@login_required
def work_home(request):
    worktasks = WorkTask.objects.order_by('type')
    return render(request, 'work/work_home.html', {'worktasks': worktasks})

@login_required
def work_closed(request):
    worktasks_cl = WorkTask.objects.order_by('type')
    return render(request, 'work/work_closed.html', {'worktasks_cl': worktasks_cl})


class WorktaskDetailView(DetailView):
    model = WorkTask
    template_name = 'work/descr_view.html'
    context_object_name = 'taska'