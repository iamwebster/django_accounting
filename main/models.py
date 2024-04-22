from django.db import models


class Stock(models.Model):
    '''Склады для хранения'''
    name = models.CharField(max_length=255)
    address = models.TextField()
    capacity = models.PositiveBigIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 


class Category(models.Model):
    '''Категории оборудования'''
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name 


class Equipment(models.Model):
    '''Информация о единицах оборудования'''
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255, default='01')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50, null=True, blank=True)
    manufacturer = models.CharField(max_length=255)
    purchase_date = models.DateField()

    def __str__(self):
        return f'{self.name} | {self.model} | {self.manufacturer}'
    