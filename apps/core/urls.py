from django.urls import path

from .views import core

app_name = 'core'
urlpatterns = [
    path('', core.index, name='index'),
    path('create/', core.create, name='create'),
    path('<int:pk>/update/', core.update, name='update'),
    path('<int:pk>/delete/', core.delete, name='delete'),
]
