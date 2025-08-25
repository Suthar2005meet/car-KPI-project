from django.contrib import admin # type: ignore
from .models import Car # type: ignore

admin.site.register(Car)
