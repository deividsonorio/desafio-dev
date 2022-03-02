from django.db import models


class Transaction(models.Model):
    class Types(models.IntegerChoices):
        DEBITO = 1
        BOLETO = 2
        FINANCIAMENTO = 3
        CREDITO = 4
        RECEBIMENTO_EMPRESTIMO = 5
        VENDAS = 6
        RECEBIMENTO_TED = 7
        RECEBIMENTO_DOC = 8
        ALUGUEL = 9

    type = models.IntegerField(choices=Types.choices)
    description = models.CharField(max_length=60)
    NATURES = (
        ('INCOMING', 'Incoming'),
        ('OUTGOING', 'Outgoing'),
    )
    nature = models.CharField(max_length=8, choices=NATURES)
    SIGNS = (
        ('+', 'Plus'),
        ('-', 'Minus'),
    )
    sign = models.CharField(max_length=1, choices=SIGNS)


class Cnab(models.Model):
    type = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    date = models.CharField(max_length=8)
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.CharField(max_length=6)
    shop_owner = models.CharField(max_length=14)
    shop_name = models.CharField(max_length=19)
    # media = models.FileField(null=True, blank=True)
