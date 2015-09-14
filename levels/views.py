from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Requirement, Category


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
    items = Requirement.objects.filter(number__number=id)
    return render(request, 'level_detail.html', {
        'level_nr': id,
        'items': items
    })


def get_category(request, name=None):
    if name is None:
        items = Category.objects.all()
        return render(request, 'category_list.html', {
            'items': items,
            })
    items = Requirement.objects.filter(category__version=name)
    return render(request, 'category_detail.html', {
        'cat': name,
        'items': items
        })
