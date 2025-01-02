from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'title' :'Tea Shop - Главная',
        'content' : 'Заходи в мой кишлак - будешь жирный как ишак',
    }
    return render(request, 'main/index.html', context)

def about_us(request) -> HttpResponse:
    categories = Categories.objects.all()

    context: dict[str, str] = {
        'title' : 'tea Shop - О нас',
        'content' : 'Тут ты можешь тренироваться, братан',
        'categories' : categories,
    }
    return render(request, 'main/about_us.html', context)