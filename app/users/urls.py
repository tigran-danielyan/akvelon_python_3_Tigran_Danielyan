from django.urls import path
from users.views.users import UserViewSet
from users.views.transactions import UserTransactionViewSet

urlpatterns = [
    # user endpoints
    path("users/", UserViewSet.as_view({
                                        'get': 'list',
                                        'post': 'create'})),
    path("users/<int:user_id>/", UserViewSet.as_view({'get': 'retrieve',
                                                      'patch': 'update',
                                                      'delete': 'destroy'
                                                      })),
    # User transaction endpoints
    path("users/<int:user_id>/transactions/", UserTransactionViewSet.as_view({'post': 'create',
                                                                              'get': 'list'})),
    path("users/<int:user_id>/grouped-transactions/", UserTransactionViewSet.as_view({'get': 'get_user_transactions'})),
    path("users/<int:user_id>/transactions/<int:transaction_id>/", UserTransactionViewSet.as_view({
                                                                    'get': 'retrieve',
                                                                    'patch': 'update',
                                                                    'delete': 'destroy'
                                                                    })),


]
