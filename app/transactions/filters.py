from django_filters import rest_framework as filters
from transactions.models import Transaction


class UserTransactionFilter(filters.FilterSet):
    method = filters.NumberFilter(lookup_expr='iexact')
    date = filters.DateFromToRangeFilter(field_name="date")

    class Meta:
        model = Transaction
        fields = ['date', 'method']
