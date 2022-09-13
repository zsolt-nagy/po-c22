from django.contrib import admin
from .models import PurchaseOrder

class PurchaseOrderAdmin(admin.ModelAdmin):
   list_display = ('company_id', 'description', 'amount', 'start_date', 'end_date')

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)