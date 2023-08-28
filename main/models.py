from django.db import models


class Curse(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='curse/', verbose_name='картинка', null=True, blank=True)
    description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='lesson/', verbose_name='картинка', null=True, blank=True)
    description = models.CharField(max_length=100, verbose_name='описание')
    url = models.URLField(max_length=50, verbose_name='ссылка на видео')

    def __str__(self):
        return f"{self.title} {self.description} {self.url}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
