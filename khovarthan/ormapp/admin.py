from django.contrib import admin

# Register your models here.
from .models import items,itemsAdmin
admin.site.register(items,itemsAdmin)

