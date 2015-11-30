from django.shortcuts import render
from asvsannotation.models import AnnotationExplanation, AnnotationRequirement


def get_explanation(request, id=None):
    if id is None:
        items = AnnotationExplanation.objects.all()
        return render(request, 'annotation_list.html', {
            'items': items
        })
    else:
        req_ann = AnnotationRequirement.objects.language().get(pk=id)
        explanation = AnnotationExplanation.objects.get(req_ann=req_ann)
        return render(request, 'annotation_explanation.html', {
            'item': explanation,
        })
