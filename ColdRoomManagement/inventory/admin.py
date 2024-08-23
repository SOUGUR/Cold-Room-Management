from django.contrib import admin
from inventory.models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'expiry_date', 'received_date', 'added_by')
    list_filter = ('expiry_date', 'added_by')
    search_fields = ('name',)
    date_hierarchy = 'received_date'