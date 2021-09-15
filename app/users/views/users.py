from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

from users.filters import UserFilter
from users.models import User
from users.serializers.users import UserSerializer, UserUpdateSerializer


class UserViewSet(ViewSet):

    def list(self, request):
        users = User.objects.all()
        filtered = UserFilter(request.GET, queryset=users)
        queryset = filtered.qs.order_by('-created_at')
        serializer = UserSerializer(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, user_id):
        get_object_or_404(User, id=user_id).delete()

        return Response(status=status.HTTP_200_OK)
