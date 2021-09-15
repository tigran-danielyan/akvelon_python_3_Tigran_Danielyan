from django.urls import path
from transactions.views import TransactionViewSet

urlpatterns = [
    # Transactions
    path('transactions/', TransactionViewSet.as_view({'get': 'list'}))

]
