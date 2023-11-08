from django.db import models

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

    
    def __str__(self):
        return self.t


