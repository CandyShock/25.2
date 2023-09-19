from rest_framework.pagination import PageNumberPagination


class LessonAndCursePagination(PageNumberPagination):
    page_size = 10
