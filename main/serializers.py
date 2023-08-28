from rest_framework import serializers

from main.models import Curse, Lesson


class CurseSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = '__all__'


class LessonSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
