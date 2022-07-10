from django.contrib import admin


from finance.models import Spending


@admin.register(Spending)
class SpendingAdmin(admin.ModelAdmin):
    list_display = ('description', 'value')
    # list_display_links = ('title', 'author')
    # list_filter = ('author',)
    list_per_page = 20
    list_max_show_all = 100
    empty_value_display = 'Vazio'
    search_fields = ['description']

    # QUAIS CAMPOS DEVE APARECER/REMOVER DA TELA DE EDIÇÃO
    # fields = (('first_name', 'last_name'), 'seniority')
    # exclude = ('first_name', 'last_name')
