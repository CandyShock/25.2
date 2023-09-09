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

    curse = models.ForeignKey(Curse, on_delete=models.CASCADE, null=True, blank=True, related_name='lesson')

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
