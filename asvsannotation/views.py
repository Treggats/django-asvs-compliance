from django.shortcuts import render
from asvs.settings import LANGUAGE_CODE
from asvsannotation.models import AnnotationExplanation, AnnotationRequirement


def get_explanation(request, id=None):
    if id is None:
        items = AnnotationExplanation.objects.all()
        return render(request, 'annotation_list.html', {
            'items': items
        })
    else:
        explanation = AnnotationExplanation.objects.get(pk=id)
        return render(request, 'annotation_explanation.html', {
            'req': explanation.req_ann,
            'info': explanation,
        })
