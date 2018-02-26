from django.contrib import admin
from .models import Course, Currency, CurrencyGroup

# Register your models here.
admin.site.register(Course)
admin.site.register(Currency)
admin.site.register(CurrencyGroup)