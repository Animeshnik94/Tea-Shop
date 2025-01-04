from django import template
from goods.models import Categories
from goods.models import Products

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag()
def tag_bestsellers():
    bestsellers = Products.objects.order_by('-quantity')[:6]
    grouped_bestsellers = [bestsellers[i:i + 3] for i in range(0, len(bestsellers), 3)]
    return grouped_bestsellers