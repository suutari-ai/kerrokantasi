from kk.enums import SectionType, Commenting
from kk.models import Section, SectionImage
from kk.utils.drf_enum_field import EnumField
from kk.views.base import BaseImageSerializer
from rest_framework import serializers, viewsets


class SectionImageSerializer(BaseImageSerializer):
    class Meta:
        model = SectionImage
        fields = ['title', 'url', 'width', 'height', 'caption']


class SectionSerializer(serializers.ModelSerializer):
    """
    Serializer for section instance.
    """
    images = SectionImageSerializer.get_field_serializer(many=True, read_only=True)
    type = EnumField(enum_type=SectionType)
    commenting = EnumField(enum_type=Commenting)

    class Meta:
        model = Section
        fields = [
            'id', 'type', 'commenting',
            'title', 'abstract', 'content', 'created_at', 'created_by', 'images', 'n_comments'
        ]


class SectionFieldSerializer(serializers.RelatedField):
    """
    Serializer for section field. A property of other instance.
    """

    def to_representation(self, section):
        return SectionSerializer(section, context=self.context).data


class SectionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SectionSerializer

    def get_queryset(self):
        return Section.objects.filter(hearing_id=self.kwargs["hearing_pk"])
