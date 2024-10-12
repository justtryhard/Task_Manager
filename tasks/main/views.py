from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required                     #запрет на вход неавторизованным пользователям
def index(request):
    data = {
        'title': 'Важная информация'
    }

    return render(request, 'main/index.html', data)


def logging_out(request):        #переход на страницу выхода
    logout(request)
    return render(request, 'registration/log_out.html')


def login(request):                  #переход на страницу авторизации
    return render(request, 'registration/login.html')


