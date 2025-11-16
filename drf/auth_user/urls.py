from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

from auth_user.views import UserTokenObtainPairView, AuthUserViewSet


auth_router = DefaultRouter()

auth_router.register(
    prefix="users",
    viewset=AuthUserViewSet,
    basename='user'
)

urlpatterns = [
    path('token/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]