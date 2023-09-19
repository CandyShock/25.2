from django.urls import path

from main.apps import MainConfig
from rest_framework.routers import DefaultRouter

from main.views import CurseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, PaymentsCreateAPIView, PaymentsListPIView, SubListAPIView, SubCreateAPIView, \
    SubRetrieveAPIView

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'Curse', CurseViewSet, basename='curse')

urlpatterns = [
                  path('Lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('Lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('Lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
                  path('Lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('Lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
                  path('Payments/', PaymentsListPIView.as_view(), name='payment_list'),
                  path('Payments/create/', PaymentsCreateAPIView.as_view(), name='payment_create'),
                  path('Sub/', SubListAPIView.as_view(), name='sub_list'),
                  path('Sub/create/', SubCreateAPIView.as_view(), name='sub_create'),
                  path('Sub/<int:pk>/', SubRetrieveAPIView.as_view(), name='sub_retrieve')
              ] + router.urls
