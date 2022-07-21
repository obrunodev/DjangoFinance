from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('finance/', include('finance.urls')),
    path('user/', include('user.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
