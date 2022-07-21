from django.contrib import admin

from finance.models import Category, Income

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Income)
class AdminIncome(admin.ModelAdmin):
    list_display = ('description', 'expected_value', 'real_value', 'day_recurrency', 'category')
    list_filter = ('day_recurrency', 'category')
    ordering = ('day_recurrency',)
    search_fields = ('description',)
