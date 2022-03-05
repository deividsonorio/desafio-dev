import time

from django.shortcuts import render
from .forms import UploadFileForm, GenerateRandomUserForm
from .tasks import create_random_user_accounts, handle_cnab_file
from .models import Cnab, Transaction
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.conf import settings


def handle_uploaded_file(f):
    name = f.name
    with open(settings.MEDIA_ROOT + time.strftime("%Y%m%d-%H%M%S") + "-" + name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return destination.name


class SaveCnabFileView(FormView):
    template_name = 'cnab/cnab_upload.html'
    form_class = UploadFileForm

    def form_valid(self, form):
        file_save = handle_uploaded_file(self.request.FILES['file'])
        handle_cnab_file.delay(file_save)
        messages.success(self.request, 'Arquivo enviado para processamento. {}'.format(file_save))
        return redirect('cnab_upload')

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return redirect('cnab_upload')


def index(request):
    if "GET" == request.method:
        form = UploadFileForm()

        return render(request, 'cnab/cnab_upload.html', {'form': form})
    else:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            message = handle_cnab_file(request.FILES['file'])
        else:
            message = "Envie um arquivo txt no padrão CNAB."

        return render(request, 'cnab/cnab_upload.html', {'form': form, 'message': message})


# returns a list of generated user accounts
class UsersListView(ListView):
    template_name = 'cnab/user_list.html'
    model = User


# A page with the form where we can input the number of accounts to generate
class GenerateRandomUserView(FormView):
    template_name = 'cnab/generate_random_user.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total=total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')
