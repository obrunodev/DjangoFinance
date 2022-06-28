from django.urls import path

from .views import categories
from .views import finance

app_name = 'finance'
urlpatterns = [
    path('', finance.index, name='index'),
    path('create/', finance.create, name='create'),

    path('categories/', categories.index, name='categories_index'),
    path('categories/<int:pk>/delete/', categories.delete, name='categories_delete'),
]
