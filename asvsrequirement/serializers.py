from asvsrequirement.models import Requirement
from rest_framework import serializers


class RequirementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Requirement
        fields = ('requirement_number', 'requirement_title',
            'category_version', 'category_title', 'level_number')
