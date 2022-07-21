from django.urls import path

from . import views

app_name = 'finance'
urlpatterns = [
    path('', views.dashboard_index, name='dashboard_index'),

    path('income/', views.income_index, name='income_index'),
]
