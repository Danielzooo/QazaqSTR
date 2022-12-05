from django.contrib.auth import logout

from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework_simplejwt.tokens import RefreshToken

from const.abstract import CustomUser
from const.permissions import IsOwnerOrIsStaff
from .const.serializers import (
    CustomUserAllFieldsSerializer,
    CustomUserCreateSerializer,
    CustomUserListSerializer,
    CustomUserLoginSerializer,
)


class CustomUserViewSet(viewsets.GenericViewSet,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserAllFieldsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permission_classes = self.permission_classes

        if self.action == 'create' or self.action == 'login':
            permission_classes = [AllowAny]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwnerOrIsStaff]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'create':
            serializer_class = CustomUserCreateSerializer
        elif self.action == 'list':
            serializer_class = CustomUserListSerializer
        elif self.action == 'login':
            serializer_class = CustomUserLoginSerializer
        return serializer_class

    @action(methods=['post'], detail=False, url_path='login')
    def login(self,  request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        response = CustomUserListSerializer(user).data
        response.__setitem__('tokens', self.get_tokens_for_user(user))

        return Response(data=response, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='verify_otp')
    def verify_otp(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = CustomUserListSerializer(serializer.validated_data['user']).data
        response.__setitem__('tokens', self.get_tokens_for_user(serializer.validated_data.get('user')))
        return Response(data=response, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='logout')
    def logout(self, request, *args, **kwargs):
        new_tokens = self.get_tokens_for_user(request.user)
        logout(request)
        return Response(data={'DETAIL': "User is Logged Out!"})

    def get_tokens_for_user(self, user: CustomUser):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }