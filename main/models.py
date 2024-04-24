from django.db import models


class Stock(models.Model):
    '''Склады для хранения'''
    name = models.CharField(max_length=255, verbose_name='Наименование склада')
    address = models.TextField(verbose_name='Адрес')
    capacity = models.PositiveBigIntegerField(verbose_name='Вместимость')
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.name 


class Category(models.Model):
    '''Категории оборудования'''
    name = models.CharField(max_length=255, verbose_name='Наименование категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name 


class Equipment(models.Model):
    '''Информация о единицах оборудования'''
    name = models.CharField(max_length=255, verbose_name='Наименование оборудования')
    model = models.CharField(max_length=255, default='01', verbose_name='Модель')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, verbose_name='Склад')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')
    receipt_date = models.DateField(verbose_name='Дата поступления')

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return f'{self.name} | {self.model} | {self.manufacturer}'
    