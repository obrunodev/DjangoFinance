from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.name


class Spending(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, verbose_name='Descrição')
    expected_cost = models.FloatField(verbose_name='Custo esperado')
    real_cost = models.FloatField(verbose_name='Custo real')
    difference = models.FloatField(verbose_name='Diferença')

    def __str__(self):
        return self.description
