from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

def index(request) -> HttpResponse:
    categories = Categories.objects.all()

    context: dict[str, str] = {
        'title' :'Tea Shop - Главная',
        'content' : 'Заходи в мой кишлак - будешь жирный как ишак',
        'categories' : categories,
    }
    return render(request, 'main/index.html', context)

def about_us(request) -> HttpResponse:
    context: dict[str, str] = {
        'title' : 'tea Shop - О нас',
        'content' : 'Тут ты можешь тренировать js, братан',
    }
    return render(request, 'main/about_us.html', context)