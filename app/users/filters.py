from django_filters import rest_framework as filters
from users.models import User


class UserFilter(filters.FilterSet):
    user_id = filters.CharFilter(lookup_expr='iexact', field_name="id")
    first_name = filters.CharFilter(lookup_expr='iexact')
    last_name = filters.CharFilter(lookup_expr='iexact')
    email = filters.CharFilter(lookup_expr='iexact')
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = User
        fields = ['user_id', 'created_at', 'first_name', 'last_name', 'email']
