from django.urls import path

from .views import finance

app_name = 'finance'
urlpatterns = [
    path('', finance.index, name='index'),
]
