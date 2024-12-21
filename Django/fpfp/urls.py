from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, LoginView, CurrentUserView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/users/me/', CurrentUserView.as_view(), name='current_user'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)