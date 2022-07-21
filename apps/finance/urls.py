from django.urls import path

from . import views

app_name = 'finance'
urlpatterns = [
    path('', views.dashboard_index, name='dashboard_index'),

    path('income/', views.income_index, name='income_index'),
    path('income/manage/', views.income_manage, name='income_manage'),
]
