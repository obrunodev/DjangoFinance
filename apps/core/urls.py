from django.urls import path

from .views import redirect_to_home

app_name = 'core'
urlpatterns = [
    path('', redirect_to_home, name='redirect_to_home'),
]
