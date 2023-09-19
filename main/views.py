from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from main.models import Curse, Lesson, Payments, subscription
from main.paginators import LessonAndCursePagination
from main.permissions import IsModer, IsOwner, IsPublic
from main.serializers import CurseSerialaizer, LessonSerialaizer, PaymentSerialaizer, SubSerialaizer


class CurseViewSet(viewsets.ModelViewSet):
    """Создавать курсы может только авторизованный пользователь"""
    serializer_class = CurseSerialaizer
    queryset = Curse.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonAndCursePagination


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerialaizer
    permission_classes = [IsAuthenticated]


class LessonListAPIView(generics.ListAPIView):
    """Просматривать список уроков может только авторизованный пользователь"""
    serializer_class = LessonSerialaizer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonAndCursePagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Смотреть детализацию может только владелец или модер"""
    """Если материал не является публичным, просматривать его может только владелец, либо модер"""
    serializer_class = LessonSerialaizer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner | IsPublic]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Обновлять может только владелец или менеджер"""
    serializer_class = LessonSerialaizer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """удалять может только владелец"""
    serializer_class = LessonSerialaizer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerialaizer


class PaymentsListPIView(generics.ListAPIView):
    serializer_class = PaymentSerialaizer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson', 'curse', 'pay_way')
    ordering_fields = ('pay_day')


class SubListAPIView(generics.ListAPIView):
    serializer_class = SubSerialaizer
    queryset = subscription.objects.all()


class SubCreateAPIView(generics.CreateAPIView):
    """создавать новые типы подписок может только модер"""
    serializer_class = SubSerialaizer
    permission_classes = [IsAuthenticated]


class SubRetrieveAPIView(generics.RetrieveAPIView):
    """Просматривать подписки может только их владелец, либо модер"""
    serializer_class = SubSerialaizer
    queryset = subscription.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModer]