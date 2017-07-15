from django.http import Http404
from rest_framework import viewsets, mixins, generics
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response

from asvsrequirement.models import Requirement
from asvsrequirement.serializers import RequirementSerializer


class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class RequirementList(generics.ListCreateAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class RequirementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
