from django.contrib import admin

from .models import Category
from .models import Spending

admin.site.register(Category)
admin.site.register(Spending)
