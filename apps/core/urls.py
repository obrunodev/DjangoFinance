from django.urls import path

from .views import core

app_name = 'core'
urlpatterns = [
    path('', core.index, name='index'),
]
