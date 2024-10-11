from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required
def index(request):
    data = {
        'title': 'Объявления'
    }

    return render(request, 'main/index.html', data)


def logging_out(request):
    logout(request)
    return render(request, 'registration/log_out.html')


def login(request):
    return render(request, 'registration/login.html')


