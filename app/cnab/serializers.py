from abc import ABC
from rest_framework.serializers import Serializer, FileField


# Upload form serializer
class UploadSerializer(Serializer):
    arquivo_cnab = FileField()

    class Meta:
        fields = ['arquivo_cnab']
