from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from asvs.settings import LANGUAGE_CODE
from asvsrequirement.models import Requirement, Category, Level
from asvsannotation.models import AnnotationRequirement, AnnotationExplanation


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        context['text'] = 'text from flatpage'
        return context


class LevelList(ListView):
    model = Requirement
    template_name = 'requirement_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        self.level = get_object_or_404(Level, level_number=self.args[0])
        return Requirement.objects.language(LANGUAGE_CODE).filter(levels=self.level)


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
