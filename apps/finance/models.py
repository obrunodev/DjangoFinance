from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField('Nome', max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Income(BaseModel):
    description = models.CharField('Descrição', max_length=256)
    expected_value = models.FloatField('Valor esperado')
    real_value = models.FloatField('Valor real')
    day_recurrency = models.IntegerField('Dia recorrente')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 verbose_name='Categoria',
                                 related_name='incomes')
    
    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Renda'
        verbose_name_plural = 'Rendas'
