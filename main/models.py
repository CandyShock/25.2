from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Curse(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='curse/', verbose_name='картинка', null=True, blank=True)
    description = models.CharField(max_length=100, verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    is_public = models.BooleanField(default=False)

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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    is_public = models.BooleanField(default=False)

    curse = models.ForeignKey(Curse, on_delete=models.CASCADE, related_name='lesson', **NULLABLE)

    def __str__(self):
        return f"{self.title} {self.description} {self.url}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payments(models.Model):
    user = models.CharField(max_length=30, verbose_name='пользователь')
    pay_day = models.DateField(max_length=30, verbose_name='дата оплаты')
    pay_check = models.BooleanField(verbose_name='оплата курса или урока', default=True)
    pay_summ = models.IntegerField(verbose_name='сумма оплаты')
    pay_way = models.CharField(max_length=40, verbose_name='способ оплаты')

    curse = models.ForeignKey(Curse, on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user} {self.pay_summ}"

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'


class subscription(models.Model):
    """подписка привязана к владельцу, отображается как и уроки списком в листе курсов под меткой sub_stat"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    sub_name = models.CharField(max_length=25, verbose_name='название подписки', **NULLABLE)
    sub_curse = models.ForeignKey(Curse, on_delete=models.CASCADE, related_name='sub_stat', **NULLABLE)
    sub_status = models.BooleanField(default=True, verbose_name='признак подписки')
