from django.urls import path
from . import views

urlpatterns = [
    path('', views.SaveCnabFileView.as_view(), name='cnab_upload'),
    path('users/', views.UsersListView.as_view(), name='users_list'),
    path('generate/', views.GenerateRandomUserView.as_view(), name='generate')
]
