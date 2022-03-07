from django.urls import path
from . import views
from rest_framework import routers
from .views import UploadViewSet

router = routers.DefaultRouter()
router.register('upload/', UploadViewSet, basename="upload")
