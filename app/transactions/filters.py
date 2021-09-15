from django_filters import rest_framework as filters
from transactions.models import Transaction


class UserTransactionFilter(filters.FilterSet):
    transaction_id = filters.CharFilter(lookup_expr='iexact', field_name="id")
    method = filters.NumberFilter(lookup_expr='iexact')
    date = filters.DateFromToRangeFilter(field_name="date")

    class Meta:
        model = Transaction
        fields = ['transaction_id', 'date', 'method']
