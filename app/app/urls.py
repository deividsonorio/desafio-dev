"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings
import time
from cnab.models import Cnab, Transaction
from cnab.views import UploadViewSet


def handle_uploaded_file(f):
    name = f.name
    with open(settings.MEDIA_ROOT + time.strftime("%Y%m%d-%H%M%S") + "-" + name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return destination.name


# Users Serializer.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# Cnab info Serializer.
class CnabSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cnab
        fields = ['type', 'date', 'value', 'cpf', 'card', 'hour', 'shop_owner', 'shop_name']


# Transactions Serializer.
class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['type', 'description', 'nature', 'sign']


# ViewSet with users list.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSet for cnab.
class CnabViewSet(viewsets.ModelViewSet):
    queryset = Cnab.objects.all()
    serializer_class = CnabSerializer


# ViewSet for transactions.
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# Routers provide an easy way of automatically determine the URL configuration.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('cnab_list', CnabViewSet)
router.register('transaction_list', TransactionViewSet)

router.register('upload', UploadViewSet, basename="upload")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
