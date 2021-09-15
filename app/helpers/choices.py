from django.db.models import IntegerChoices


class TransactionType(IntegerChoices):
    INCOME = 0
    WITHDRAWAL = 1
