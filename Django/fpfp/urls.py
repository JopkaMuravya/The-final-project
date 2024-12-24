from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, LoginView, CurrentUserView, TaskViewSet, UpdateBalanceView, ConfirmEmailView, MessageViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/users/me/', CurrentUserView.as_view(), name='current_user'),
    path('api/users/me/update-balance/', UpdateBalanceView.as_view(), name='update_balance'),
    path('api/', include(router.urls)),
    path('api/confirm/<uidb64>/<token>/', ConfirmEmailView.as_view(), name='confirm_email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)