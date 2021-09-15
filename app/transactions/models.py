from django.db import models
from helpers.choices import TransactionType
from users.models import User


class Transaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    method = models.IntegerField(choices=TransactionType.choices)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
