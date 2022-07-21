from django.urls import path

from .views import users

app_name = 'user'
urlpatterns = [
    path('signin/', users.signin, name='signin'),
    path('signup/', users.signup, name='signup'),
    path('signout/', users.signout, name='signout'),
    path('profile/', users.profile, name='profile'),
]
