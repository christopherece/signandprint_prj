from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'category', 'subject', 'description')
    search_fields = ('name', 'email', 'category', 'subject')
    list_filter = ('category',)

admin.site.register(Contact, ContactAdmin)