from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Lesson, subscription


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_lesson(self):
        """Тест создания урока"""
        data = {
            "url": "http://youtube.com",
            "title": "Testtest",
            "description": "tests",
        }
        response = self.client.post(
            '/Lesson/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'url': 'http://youtube.com', 'title': 'Testtest', 'preview': None, 'description': 'tests',
             'is_public': False, 'owner': None, 'curse': None}
        )

        self.assertTrue(
            Lesson.objects.all().exists
        )


class SubTestCase(APITestCase):
    """тест на осздание подписки"""

    def setUp(self) -> None:
        pass

    def test_create_sub(self):
        """Тест создания урока"""
        data = {
            "sub_name": "Tests",
            "sub_status": 'true'
        }
        response = self.client.post(
            '/Sub/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'sub_name': 'Tests', 'sub_status': True, 'owner': None, 'sub_curse': None}

        )

        self.assertTrue(
            subscription.objects.all().exists
        )

    def test_list_sub(self):
        """тест на вывод списка подписок"""
        subscription.objects.create(
            id=1,
            sub_name='Tests',
            sub_status=True
        )

        response = self.client.get(
            '/Sub/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 1, 'sub_name': 'Tests', 'sub_status': True, 'owner': None, 'sub_curse': None}]
        )
