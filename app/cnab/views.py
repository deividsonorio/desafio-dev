from django.shortcuts import render
from .forms import UploadFileForm
from .models import Cnab, Transaction


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


def handle_cnab_file(cnab_file):
    if not cnab_file.name.endswith('.txt'):
        return "Este não é um arquivo .txt"
    try:
        file_data = cnab_file.read().decode("utf-8")
        lines = file_data.split("\n")

        # loop over the lines
        for line in lines:
            transaction_type = line[0:1]
            transaction = Transaction.objects.get(type=transaction_type)

            cnab_data = {
                'type': transaction,
                'date': line[1:9],
                'value': line[9:19],
                'cpf': line[19:30],
                'card': line[30:42],
                'hour': line[42:48],
                'shop_owner': line[48:62],
                'shop_name': line[62:80],
            }

            cnab = Cnab(**cnab_data)
            cnab.save()

            return "Arquivo salvo"
    except:
        return "Houve um erro ao procesar o arquivo"

