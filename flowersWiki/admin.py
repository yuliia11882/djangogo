
from django.contrib import admin

# Register your models here.

from .models import Flower, Types

@admin.register(Flower)
class flowerAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'location']
    


@admin.register(Flower)
class flowerAdmin(admin.ModelAdmin):
    pass