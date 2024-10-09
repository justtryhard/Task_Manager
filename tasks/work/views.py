from django.shortcuts import render
from .models import WorkTask


def work_home(request):
    worktasks = WorkTask.objects.all()
    return render(request, 'work/work_home.html', {'worktasks': worktasks})
