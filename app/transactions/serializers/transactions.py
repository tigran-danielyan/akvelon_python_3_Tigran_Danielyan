from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from transactions.models import Transaction


def validate_amount(obj):
    if obj < 0:
        raise ValidationError("amount shouldn't be negative")


class TransactionSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField(validators=[validate_amount])

    class Meta:
        model = Transaction
        exclude = ('user',)


class TransactionUpdateSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField(validators=[validate_amount])

    def validate(self, attrs):
        if attrs['amount'] < 0:
            raise ValidationError("amount shouldn't be negative")

    class Meta:
        model = Transaction
        fields = ('amount', 'method')


class TransactionSummarySerializer(serializers.Serializer):
    method = serializers.IntegerField()
    day = serializers.DateTimeField()
    sum = serializers.FloatField()
