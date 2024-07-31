from django.db import models

class orders(models.Model):
    name = models.TextField('Имя', max_length='15', blank=True)
    tel = models.CharField('Телефон', max_length=12,  blank=True)
    comments = models.TextField('Комментарий', max_length='60')
    date = models.DateField('Дата заявки', auto_now=True)

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'
