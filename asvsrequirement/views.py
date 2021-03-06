from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from asvs.settings.base import LANGUAGE_CODE
from asvsrequirement.models import Requirement, Category, Level
from asvsannotation.models import Annotation


class HomeView(TemplateView):
    template_name = 'index.html'


class NotFoundView(TemplateView):
    template_name = '404.html'


class LevelListView(ListView):
    model = Requirement
    context_object_name = 'items'

    def get_queryset(self):
        self.level = get_object_or_404(Level, level_number=self.args[0])
        return Requirement.objects.language(LANGUAGE_CODE).filter(
            levels=self.level)


class CategoryListView(ListView):
    model = Category
    context_object_name = 'items'


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        requirements = Requirement.objects.language(LANGUAGE_CODE).filter(
            category=context['object'])
        context['category'] = context['object']
        context['items'] = requirements
        return context

    def get_object(self):
        """Returns the Category instance that the view displays"""
        return get_object_or_404(Category, category_number=self.kwargs.get(
            "category_number"))


class RequirementListView(ListView):
    model = Requirement
    context_object_name = 'items'


class RequirementDetailView(DetailView):
    model = Requirement
    context_object_name = 'requirement'

    def get_queryset(self):
        return Requirement.objects.language(LANGUAGE_CODE).filter(
            pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super(RequirementDetailView, self).get_context_data(**kwargs)
        context['category'] = context['object'].category
        context['level'] = context['object'].level_number
        context['annotations'] = Annotation.objects.language(
                LANGUAGE_CODE).filter(requirement=context['object'])

        return context
