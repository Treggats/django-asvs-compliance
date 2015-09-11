from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Requirement


def index(request):
    return render(request, 'index.html', {
        'cat_1': reverse('get_category', args=[1]),
        'cat_2': reverse('get_category', args=[2]),
        'cat_3': reverse('get_category', args=[3])
        })


def get_requirement(request, id):
    items = Requirement.objects.select_related('category__name')
    item = items.get(pk=id)
    return render(request, 'get_requirement.html', {
        'item': item,
        'category': item.category,
        'level': item.level_verbose()
    })


def get_category(request, id=None):
    pass
