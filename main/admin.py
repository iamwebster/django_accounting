from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.apps import AuthConfig

from .models import Stock, Category, Equipment


class EquipmentInline(admin.StackedInline):
    model = Equipment
    extra = 1


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity', 'is_active']
    search_fields = ['name', 'address', 'capacity']
    list_filter = ['is_active', 'capacity']
    save_on_top = True
    inlines = [EquipmentInline,]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name', 'description']
    save_on_top = True
    inlines = [EquipmentInline,]


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'manufacturer', 'quantity']
    search_fields = ['name', 'model', 'manufacturer']
    list_filter = ['category__name', 'stock__name',]


AuthConfig.verbose_name = 'Пользователи'

admin.site.unregister(Group)
