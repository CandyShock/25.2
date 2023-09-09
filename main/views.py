from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from main.models import Curse, Lesson, Payments
from main.serializers import CurseSerialaizer, LessonSerialaizer, PaymentSerialaizer


class CurseViewSet(viewsets.ModelViewSet):
    serializer_class = CurseSerialaizer
    queryset = Curse.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerialaizer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerialaizer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerialaizer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerialaizer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerialaizer
    queryset = Lesson.objects.all()


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerialaizer


class PaymentsListPIView(generics.ListAPIView):
    serializer_class = PaymentSerialaizer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson', 'curse', 'pay_way')
    ordering_fields = ('pay_day')
