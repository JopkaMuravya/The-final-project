from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, LoginView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/', include(router.urls)),
]
