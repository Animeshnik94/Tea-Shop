from django.shortcuts import render
from django.http import HttpResponse

def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'title' :'Tea Shop - Главная',
        'content' : 'Заходи в мой кишлак - будешь жирный как ишак',
    }
    return render(request, 'main/index.html', context)

def about_us(request) -> HttpResponse:
    context: dict[str, str] = {
        'title' : 'tea Shop - О нас',
        'content' : 'Тут ты можешь тренировать js, братан',
    }
    return render(request, 'main/about_us.html', context)