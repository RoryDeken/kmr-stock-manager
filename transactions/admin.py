from django.contrib import admin
from .models import (
    Supplier, 
    PurchaseBill, 
    PurchaseItem,
    PurchaseBillDetail, 
    SaleBill, 
    SaleItem,
    SaleBillDetail
)

admin.site.register(Supplier)
admin.site.register(PurchaseBill)
admin.site.register(PurchaseItem)
admin.site.register(PurchaseBillDetail)
admin.site.register(SaleBill)
admin.site.register(SaleItem)
admin.site.register(SaleBillDetail)