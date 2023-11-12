from django.db import models


class Region(models.Model):
    class Meta:
        verbose_name = 'Регіон'
        verbose_name_plural = 'Регіони'
        
    name = models.CharField(max_length=255, verbose_name = 'Назва')

    def __str__(self):
        return self.name

class Agency(models.Model):
    class Meta:
        verbose_name = 'Установа'
        verbose_name_plural = 'Установи'

    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name = 'Регіон')
    name = models.CharField(max_length=255, verbose_name = 'Назва')
    edrpou = models.CharField(max_length=20, unique=True, verbose_name = 'ЕДРПОУ')

    def __str__(self):
        return self.name

class Tender(models.Model):
    class Meta:
        verbose_name = 'Тендер'
        verbose_name_plural = 'Тендери'
        ordering = ["-a"]

    t = models.CharField(max_length=255, verbose_name = 'Заголовок')
    tl = models.URLField(max_length=255, unique=True, verbose_name = 'URL')
    cpv = models.CharField(max_length=255, blank=True, verbose_name = 'CPV')
    v = models.FloatField(blank=True, verbose_name = 'Очікувана вартість закупівлі')
    a = models.DateTimeField(blank=True, null=True, verbose_name = 'Дата оголошення процедури')
    s = models.CharField(max_length=255, blank=True, verbose_name = 'Поточний статус процедури')
    t_id = models.CharField(max_length=255, unique=True, verbose_name = 'Ідентифікатор закупівлі')
    cdb = models.CharField(max_length=255, verbose_name = 'Організатор закупівлі')
    t_method = models.CharField(max_length=255, verbose_name = 'Процедура закупівлі')
    edr = models.ForeignKey(Agency, on_delete=models.CASCADE, to_field='edrpou', default='00022504', verbose_name = 'Код ЄДРПОУ')

    
    def __str__(self):
        return self.t


