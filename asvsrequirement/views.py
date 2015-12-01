from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from asvs.settings import LANGUAGE_CODE
from django.core.urlresolvers import reverse 
from asvsrequirement.models import Requirement, Category, Level
from asvsannotation.models import AnnotationExplanation


class LevelList(ListView):
    model = Requirement
    template_name = 'requirement_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        self.level = get_object_or_404(Level, level_number=self.args[0])
        return Requirement.objects.language(LANGUAGE_CODE).filter(levels=self.level)


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
        items = Requirement.objects.language().select_related('category')
        item = items.get(pk=id)
        ae_items = AnnotationExplanation.objects.all()
        info = ae_items.filter(req_ann__requirement__requirement_number__exact=item.requirement_number).filter(req_ann__category__exact=item.category)

        return render(request, 'requirement_detail.html', {
            'item': item,
            'category': item.category,
            'level': ", ".join([str(level.get('level_number')) for level in item.levels.values()]),
            'info': info
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
