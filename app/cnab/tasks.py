from celery import shared_task
from .models import Cnab, Transaction
import logging
logger = logging.getLogger(__name__)


@shared_task(name="handle_cnab_file")
def handle_cnab_file(cnab_file):

    with open(cnab_file, encoding='utf8') as lines:
        # loop over the lines
        for line in lines:
            transaction_type = line[0:1]
            transaction = Transaction.objects.get(type=transaction_type)

            shop_owner = line[48:62]
            shop_name = line[62:80]

            cnab_data = {
                'type': transaction,
                'date': line[1:9],
                'value': line[9:19],
                'cpf': line[19:30],
                'card': line[30:42],
                'hour': line[42:48],
                'shop_owner': shop_owner.strip(),
                'shop_name': shop_name.strip(),
            }
            cnab = Cnab(**cnab_data)
            cnab.save()

            logger.info('Arquivo processado: {}'.format(cnab_file))
