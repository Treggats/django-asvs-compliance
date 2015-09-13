from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Requirement


def index(request):
    return render(request, 'index.html', {
        'cat_1': reverse('get_level', args=[1]),
        'cat_2': reverse('get_level', args=[2]),
        'cat_3': reverse('get_level', args=[3])
        })


def get_requirement(request, id):
    items = Requirement.objects.select_related('category__name')
    item = items.get(pk=id)
    return render(request, 'requirement_detail.html', {
        'item': item,
        'category': item.category,
        'level': item.level_verbose()
    })


def get_level(request, id):
    items = Requirement.objects.all()
    if id in items.level_number():
        return render(request, 'level_detail.html', {
            'items': items.level_verbose()
        })
