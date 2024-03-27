from django.contrib import admin

from apps.inline import OrderMealTranslatableTabularInline
from apps.models import Table, Meal, Order


# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')
    list_display_links = ('id', 'number')


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderMealTranslatableTabularInline]
