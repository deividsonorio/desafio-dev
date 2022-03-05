import os
import string

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
from celery import shared_task
from .models import Cnab, Transaction
import logging
logger = logging.getLogger(__name__)


@shared_task(name="create_random_user_accounts")
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)


@shared_task(name="handle_cnab_file")
def handle_cnab_file(cnab_file):

    with open(cnab_file, encoding='utf8') as lines:
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

            logger.info('Arquivo processado: {}'.format(cnab_file))
