from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True


class Spending(models.Model):
    description = models.CharField('Descrição', max_length=200)
    value = models.FloatField('Valor')

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
