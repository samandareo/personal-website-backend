from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, RegisterUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/posts/<int:pk>/increment_views/', BlogPostViewSet.as_view({'get': 'increment_views'})),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/logout', TokenBlacklistView.as_view(), name='token_blacklist'),
]

urlpatterns += [
    path('api/register/', RegisterUserView.as_view(), name='register'),
]