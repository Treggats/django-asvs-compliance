from django.shortcuts import render
from django.core.urlresolvers import reverse
from asvsannotation.models import Requirement, Category, AnnotationExplanation, \
    RequirementAnnotated


def index(request):
    return render(request, 'index.html', {
        'cat_1': reverse('get_level', args=[1]),
        'cat_2': reverse('get_level', args=[2]),
        'cat_3': reverse('get_level', args=[3])
        })


def get_requirement(request, id=None):
    if id is None:
        items = Requirement.objects.language().all()
        return render(request, 'requirement_list.html', {
            'items': items
        })
    else:
        items = Requirement.objects.language().select_related('category__name')
        item = items.get(pk=id)
        return render(request, 'requirement_detail.html', {
            'item': item,
            'category': item.category,
            'asvsrequirement': item.level_verbose()
        })


def get_level(request, id):
    items = Requirement.objects.language().filter(levels__in=id)
    return render(request, 'level_detail.html', {
        'level_nr': id,
        'items': items
    })


def get_category(request, cat_nr=None):
    if cat_nr is None:
        items = Category.objects.all()
        return render(request, 'category_list.html', {
            'items': items,
            })
    else:
        items = Requirement.objects.language().filter(
            category__category_number=cat_nr)
        category = Category.objects.language().get(category_number=cat_nr)
        return render(request, 'category_detail.html', {
            'category': category,
            'items': items
            })
