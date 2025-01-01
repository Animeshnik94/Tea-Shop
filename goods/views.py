from django.shortcuts import render
from django.http import HttpResponse


def catalog(request) -> HttpResponse:

    
    context: dict = {
        'title': 'Tea Shop-Каталог',
        'goods': [
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Зеленый чай',
                'description': 'Натуральный зеленый чай с легким вкусом.',
                'id' : 11111,
                'price': 15.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Черный чай',
                'description': 'Классический черный чай с насыщенным вкусом.',
                'id' : 11111,
                'price': 18.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Травяной чай',
                'description': 'Чай из различных трав для расслабления.',
                'id' : 11111,
                'price': 22.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Улун',
                'description': 'Полуферментированный чай с уникальным вкусом.',
                'id' : 11111,
                'price': 25.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Белый чай',
                'description': 'Нежный чай с легким цветочным ароматом.',
                'id' : 11111,
                'price': 30.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Пуэр',
                'description': 'Ферментированный чай с глубоким вкусом.',
                'id' : 11111,
                'price': 35.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Эрл Грей',
                'description': 'Черный чай с бергамотом.',
                'id' : 11111,
                'price': 20.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Матча',
                'description': 'Порошковый зеленый чай с ярким вкусом.',
                'id' : 11111,
                'price': 40.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Чай масала',
                'description': 'Ароматный индийский чай с пряностями.',
                'id' : 11111,
                'price': 28.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Имбирный чай',
                'description': 'Чай с добавлением свежего имбиря.',
                'id' : 11111,
                'price': 18.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Ромашковый чай',
                'description': 'Успокаивающий чай из ромашки.',
                'id' : 11111,
                'price': 15.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Мятный чай',
                'description': 'Чай с освежающим мятным вкусом.',
                'id' : 11111,
                'price': 17.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Фруктовый чай',
                'description': 'Чай с добавлением различных фруктов.',
                'id' : 11111,
                'price': 25.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Ройбуш',
                'description': 'Чай без кофеина с ореховым вкусом.',
                'id' : 11111,
                'price': 20.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Гибискус',
                'description': 'Кислый чай с ярким цветом.',
                'id' : 11111,
                'price': 22.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Лавандовый чай',
                'description': 'Чай с ароматом лаванды для расслабления.',
                'id' : 11111,
                'price': 24.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Белый пион',
                'description': 'Нежный белый чай с легким вкусом.',
                'id' : 11111,
                'price': 32.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Драконий колодец',
                'description': 'Классический китайский зеленый чай.',
                'id' : 11111,
                'price': 45.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Жасминовый чай',
                'description': 'Зеленый чай с жасмином.',
                'id' : 11111,
                'price': 30.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Чай в пакетиках',
                'description': 'Удобный чай в пакетиках для быстрого заваривания.',
                'id' : 11111,
                'price': 10.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Ягодный чай',
                'description': 'Чай с добавлением ягод для сладкого вкуса.',
                'id' : 11111,
                'price': 26.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Ванильный чай',
                'description': 'Чай с добавлением ванили для сладости.',
                'id' : 11111,
                'price': 27.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Миндальный чай',
                'description': 'Чай с легким миндальным ароматом.',
                'id' : 11111,
                'price': 29.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Чай с тимьяном',
                'description': 'Чай с добавлением тимьяна для аромата.',
                'id' : 11111,
                'price': 23.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Лаймовый чай',
                'description': 'Чай с добавлением лайма для свежести.',
                'id' : 11111,
                'price': 21.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Розовый чай',
                'description': 'Чай с лепестками роз для аромата.',
                'id' : 11111,
                'price': 33.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Банановый чай',
                'description': 'Чай с банановым вкусом.',
                'id' : 11111,
                'price': 19.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Кокосовый чай',
                'description': 'Чай с добавлением кокоса.',
                'id' : 11111,
                'price': 28.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Персиковый чай',
                'description': 'Чай с персиковым вкусом.',
                'id' : 11111,
                'price': 24.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Шоколадный чай',
                'description': 'Чай с добавлением шоколада.',
                'id' : 11111,
                'price': 30.00
            },
            {
                'image': 'deps/images/goods/boshki.jpg',
                'name': 'Кофейный чай',
                'description': 'Чай с кофейным вкусом.',
                'id' : 11111,
                'price': 32.00
            },
        ]
    }
    return render(request, 'goods/catalog.html', context )


def product(request):
    return render(request, 'goods/product.html') 