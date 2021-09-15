from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from transactions.models import Transaction
from transactions.serializers.transactions import TransactionSerializer
from transactions.filters import UserTransactionFilter


class TransactionViewSet(ViewSet):

    def list(self, request):
        transactions = Transaction.objects.order_by('-date')
        filtered = UserTransactionFilter(request.GET, queryset=transactions)
        serializer = TransactionSerializer(filtered.qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

