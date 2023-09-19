from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from main.models import Curse, Lesson, Payments, subscription
from main.validators import url_validator


class PaymentSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class LessonSerialaizer(serializers.ModelSerializer):
    """валидация по сслыке"""
    url = serializers.URLField(validators=[url_validator])

    class Meta:
        model = Lesson
        fields = '__all__'


class SubSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = subscription
        fields = '__all__'


class CurseSerialaizer(serializers.ModelSerializer):
    """Выводит уроки привязанные к данному курсу по id"""
    lesson = LessonSerialaizer(many=True, read_only=True)
    """Подсчет количества уроков для курса"""
    lesson_count = serializers.SerializerMethodField()
    sub_stat = SubSerialaizer(many=True, read_only=True)

    def get_lesson_count(self, obj):
        return obj.lesson.count()

    class Meta:
        model = Curse
        fields = '__all__'
