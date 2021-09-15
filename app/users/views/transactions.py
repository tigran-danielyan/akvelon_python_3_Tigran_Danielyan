from django.db.models import Sum
from django.db.models.functions import TruncDay
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from transactions.models import Transaction
from transactions.serializers.transactions import (
    TransactionSerializer,
    TransactionUpdateSerializer,
    TransactionSummarySerializer
)
from transactions.filters import UserTransactionFilter


class UserTransactionViewSet(ViewSet):

    def list(self, request, user_id):
        sorted_by = request.GET.get('amount', 'date')
        transactions = Transaction.objects.filter(user_id=user_id)
        filtered = UserTransactionFilter(request.GET, queryset=transactions).qs
        ordered = filtered.order_by('-amount') if sorted_by == 'amount' else filtered.order_by('-date')
        serializer = TransactionSerializer(ordered, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, user_id):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=user_id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, user_id, transaction_id):
        transaction = get_object_or_404(Transaction, id=transaction_id, user_id=user_id)
        serializer = TransactionSerializer(transaction)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, user_id, transaction_id):
        transaction = get_object_or_404(Transaction, id=transaction_id, user_id=user_id)
        serializer = TransactionUpdateSerializer(transaction, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, user_id, transaction_id):
        get_object_or_404(Transaction, id=transaction_id, user_id=user_id).delete()

        return Response(status=status.HTTP_200_OK)

    def get_user_transactions(self, request, user_id):
        user_transactions = Transaction.objects.filter(user_id=user_id)
        filtered = UserTransactionFilter(request.GET, queryset=user_transactions)
        qs = filtered.qs.annotate(day=TruncDay('date')).values('day', 'method')\
                        .annotate(sum=Sum('amount')).order_by('sum')

        serializer = TransactionSummarySerializer(qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
