from hashlib import blake2b
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    total_expected_cost = models.FloatField(verbose_name='Total custo previsto', default=0)
    total_real_cost = models.FloatField(verbose_name='Total custo real', default=0)
    total_difference = models.FloatField(verbose_name='Diferença total', default=0)

    def __str__(self):
        return self.name


class Spending(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    description = models.CharField(max_length=200, verbose_name='Descrição')
    expected_cost = models.FloatField(verbose_name='Custo previsto')
    real_cost = models.FloatField(verbose_name='Custo real', default=0)
    difference = models.FloatField(verbose_name='Diferença')

    def __str__(self):
        return self.description
