import time

from rest_framework import status

from .tasks import handle_cnab_file
from django.conf import settings
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import UploadSerializer


def handle_uploaded_file(f):
    name = f.name
    with open(settings.MEDIA_ROOT + time.strftime("%Y%m%d-%H%M%S") + "-" + name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return destination.name


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET - Envie arquivos txt no formato CNAB por POST", status=status.HTTP_200_OK)

    def create(self, request):
        if request.FILES.get('arquivo_cnab'):
            file_uploaded = request.FILES.get('arquivo_cnab')
            filename = file_uploaded.name
            if filename.endswith('.txt'):
                file_save = handle_uploaded_file(file_uploaded)
                handle_cnab_file.delay(file_save)
                response = 'Arquivo enviado para processamento. {}'.format(file_uploaded.name)

                return Response(response, status=status.HTTP_200_OK)
            else:
                response = 'Envie arquivo com extensão .txt. {}'.format(file_uploaded.name)

                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        return Response("Nenhum arquivo recebido", status=status.HTTP_400_BAD_REQUEST)
