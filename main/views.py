from rest_framework import viewsets, generics

from main.models import Curse, Lesson
from main.serializers import CurseSerialaizer, LessonSerialaizer


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
