from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, force_authenticate, APIRequestFactory, APITestCase
from .views import UploadViewSet


class CnabUploadTestCase(APITestCase):
    # Test Cnab upload file
    fixtures = ["transactions.json"]

    def test_api_access_not_logged(self):
        client = APIClient()
        response = client.get('http://localhost:8000/')

        self.assertEqual(response.status_code, 403, "Um status 403 deveria ser retornado")

    def test_api_access_nonexistent_user(self):
        client = APIClient()
        client.login(username='wrongname', password='wrongpass')
        response = client.get('http://localhost:8000/')

        self.assertEqual(response.status_code, 403, "Um status 200 deveria ser retornado")

    def test_api_access(self):
        client = APIClient()
        client.login(username='desafio', password='dev@pass')
        response = client.get('http://0.0.0.0:8000/')

        self.assertEqual(response.status_code, 200, "Um status 200 deveria ser retornado")

    def test_cnab_upload_not_logged(self):
        client = APIClient()
        response = client.get('http://0.0.0.0:8000/upload/')

        self.assertEqual(response.status_code, 403, "Um status 200 deveria ser retornado")

    def test_cnab_upload_get_list(self):
        user = User.objects.get(username='desafio')
        factory = APIRequestFactory()
        request = factory.get('/upload/')
        view = UploadViewSet.as_view({'get': 'list'})
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, 200, "Um status 200 deveria ser retornado")

    def test_api_wrong_extension(self):
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)

        file = SimpleUploadedFile("CNAB.doc", b"file_content", content_type="text/plain")
        response = self.client.post(reverse('upload-list'), {'arquivo_cnab': file})

        self.assertEqual(response.content, b'"Envie arquivo com extens\xc3\xa3o .txt. CNAB.doc"')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,
                         "Um arquivo de extensão errada deveria gerar um erro 400")

    def test_api_right_extension(self):
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)

        file = SimpleUploadedFile("CNAB.txt",
                                  b"3201903010000019200845152540736777****1313172712MARCOS PEREIRAMERCADO DA AVENIDA",
                                  content_type="text/plain")
        response = self.client.post(reverse('upload-list'), {'arquivo_cnab': file})

        self.assertEqual(response.content, b'"Arquivo enviado para processamento. CNAB.txt"')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         "Um arquivo txt deveria ser enviado para processamento com status 200")

    def test_api_no_file(self):
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        response = self.client.post(reverse('upload-list'))

        self.assertEqual(response.content, b'"Nenhum arquivo recebido"')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,
                         "Um post sem arquivo deveria gerar uma resposta com status 400")
