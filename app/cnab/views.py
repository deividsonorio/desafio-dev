from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from .forms import UploadFileForm
from django.shortcuts import redirect
from .models import Cnab, Transaction


def index(request):
    template = loader.get_template('cnab/cnab_upload.html')
    context = {
        'latest_question_list': 'nada',
    }
    return HttpResponse(template.render(context, request))


def upload_cnab(request):
    if "POST" == request.method:
        template = loader.get_template('cnab/cnab_upload.html')
        context = {
            'latest_question_list': 'nada',
        }
        cnab_file = request.FILES["cnab_file"]
        if not cnab_file.name.endswith('.txt'):
            return HttpResponse("não é txt")

        file_data = cnab_file.read().decode("utf-8")
        lines = file_data.split("\n")

        #loop over the lines
        for line in lines:
            cnab = {
                'transaction': line[0:1],
                'date': line[1:9],
                'value': line[10:19],
                'cpf': line[20:30],
                'card': line[31:42],
            }
            print(cnab)

        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("carregou por get")
        # if not GET, then proceed
    # try:
    #     cnab_file = request.FILES["cnab_file"]
    #     if not cnab_file.name.endswith('.txt'):
    #         messages.error(request,'File is not cnab type')
    #         return HttpResponseRedirect(reverse("cnab:upload_csv"))


    # if "POST" == request.method:
    #     return HttpResponse("Hello, world. You're at the cnab index. {}")
    # teste = 1+1
    # linha = "3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO"
    #
    # template = loader.get_template('cnab/cnab_upload.html')
    # context = {
    #     'latest_question_list': teste,
    # }
    #
    # return HttpResponse(template.render(context, request))
    # # return HttpResponse("Hello, world. You're at the cnab index. {}".format(teste))

def upload_file(request):
    message = ''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            handle_cnab_file(request.FILES['file'])
            message = 'sucesso'
    else:
        form = UploadFileForm()
    return render(request, 'cnab/cnab_upload.html', {'form': form, 'message': message})


def handle_cnab_file(cnab_file):
    if not cnab_file.name.endswith('.txt'):
        return HttpResponse("não é txt")

    file_data = cnab_file.read().decode("utf-8")
    lines = file_data.split("\n")

    #loop over the lines
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

        print(cnab_data)

        cnab = Cnab(**cnab_data)
        cnab.save()
