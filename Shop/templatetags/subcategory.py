from django import template
from ..models import *

register = template.Library()


@register.inclusion_tag('categories.html')
def subcategory():
    subcategory = SubCategory.objects.all()
    return {'subcategory': subcategory}
