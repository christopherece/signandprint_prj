from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'price_min', 'price_max', 'usage', 'image')
    search_fields = ('name', 'size', 'usage')
    list_filter = ('size',)
    ordering = ('name',)

admin.site.register(Service, ServiceAdmin)
