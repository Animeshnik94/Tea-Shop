from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Products


def catalog(request) -> HttpResponse:
    goods = Products.objects.all()
    
    context: dict = {
        'title': 'Tea Shop-Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context )


def product(request):
    return render(request, 'goods/product.html') 