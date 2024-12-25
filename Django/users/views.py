from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .serializers import UserSerializer, TaskSerializer, MessageSerializer
from .models import Task, CustomUser, Message
from decimal import Decimal
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework.decorators import action
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from .tokens import account_activation_token
from django.shortcuts import render, redirect
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser


class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            self.send_confirmation_email(request, user)
            return Response({'details': 'Confirmation email sent'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_confirmation_email(self, request, user):
        mail_subject = 'Activate your account.'
        message = f'Please click the link to activate your account: http://{get_current_site(request).domain}/api/confirm/{urlsafe_base64_encode(force_bytes(user.pk))}/{account_activation_token.make_token(user)}/'
        email = EmailMessage(mail_subject, message, to=[user.email])
        email.send()


class ConfirmEmailView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser .objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser .DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.confirm = True
            user.save()
            return redirect('http://localhost:9000/#/main')
        else:
            return Response({'details': 'Activation link is invalid!'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "message": "Вход выполнен успешно.",
                "token": token.key
            }, status=status.HTTP_200_OK)
        return Response({"error": "Неверный логин или пароль."}, status=status.HTTP_400_BAD_REQUEST)


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "avatar": user.avatar.url if user.avatar else None,
            "level": user.level,
            "rank": user.rank,
            "balance": user.balance,
        })


class UpdateBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        amount = request.data.get('amount', 0)

        try:
            amount = abs(Decimal(amount))
            if user.balance < amount:
                return Response({"error": "Недостаточно средств на балансе."}, status=status.HTTP_400_BAD_REQUEST)
            user.balance -= amount
            user.save()
            return Response({"message": "Баланс успешно обновлен.", "balance": user.balance}, status=status.HTTP_200_OK)
        except (ValueError, Decimal.InvalidOperation):
            return Response({"error": "Некорректное значение суммы."}, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser) 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def take(self, request, pk=None):
        task = self.get_object()

        if task.user == request.user:
            return Response({"error": "Нельзя брать собственное задание."}, status=status.HTTP_400_BAD_REQUEST)

        if task.executor is not None:
            return Response({"error": "Задание уже взято другим исполнителем."}, status=status.HTTP_400_BAD_REQUEST)

        task.executor = request.user
        task.save()

        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
