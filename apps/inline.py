from django.contrib.admin import TabularInline

from apps.models import OrderMeal


class OrderMealTranslatableTabularInline(TabularInline):
    model = OrderMeal
