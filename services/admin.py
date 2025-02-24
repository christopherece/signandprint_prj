from django.contrib import admin
from .models import Service, Item


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')
    list_filter = ('name',)
    ordering = ('name',)

admin.site.register(Service, ServiceAdmin)


# Register the Item model
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'price', 'image')  # Columns to display in the admin list view
    search_fields = ('name', 'service__name')  # Enable searching by item name or service name

# Register the models to the admin site
admin.site.register(Item, ItemAdmin)
