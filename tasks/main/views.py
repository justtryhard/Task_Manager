from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from .forms import Advert, AdvertForm


def support_check(user): # проверка, что юзер является саппортом
    return user.is_superuser or user.groups.filter(name='Support').exists()


@login_required  #запрет на вход неавторизованным пользователям
def index(request):
    data = {
        'title': 'Важная информация'
    }
    adverts = Advert.objects.order_by('-create_date')
    return render(request, 'main/index.html', {'adverts': adverts})


def logging_out(request):  #переход на страницу выхода
    logout(request)
    return render(request, 'registration/log_out.html')


def login(request):  #переход на страницу авторизации
    return render(request, 'registration/login.html')


@user_passes_test(support_check)
@login_required
def create_adv(request):    # изъятие данных из формы и передача в БД
    error = ''
    if request.method == 'POST':
        form = AdvertForm(request.POST)
        if form.is_valid():
            adv = form.save(commit=False)
            adv.author = request.user
            adv.save()
            return redirect('home')
        else:
            error = 'Неверная форма'

    form = AdvertForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_adv.html', data)
