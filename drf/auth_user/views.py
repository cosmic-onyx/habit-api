from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from auth_user.serializers import UserTokenObtainPairSerializer
from auth_user.models import AuthUser
from auth_user.serializers import UserSerializer, CreateUserSerializer


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer


class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    permission_classes = [AllowAny]
    ordering_fields = '__all__'
    search_fields = ('telegram_id', 'username')
    filterset_fields = ('telegram_id', 'username')

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return UserSerializer