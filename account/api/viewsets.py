from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from django.contrib.auth.hashers import make_password
from account.models import User
from .serializers import UserSerializer, RegisterUserSerializer, LogoutUserSerializer


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'full_name', 'first_name', 'last_name', 'email', 'phone']
    http_method_names = ['get']

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)


class RegisterUserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'id': serializer.data.get('id'),
                'email': serializer.data.get('email'),
                'name': serializer.data.get('first_name', None),
                'registered': True
            }, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        password = serializer.validated_data.get('password', None)
        if password:
            serializer.validated_data['password'] = make_password(password)
        serializer.save()


class LogoutUserViewSet(ModelViewSet):

    serializer_class = LogoutUserSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    http_method_names = ['get']

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)

    def list(self, request, *args, **kwargs):
        if request.user.id:
            request.user.auth_token.delete()
        return Response({'Logout': True}, status=status.HTTP_200_OK)
