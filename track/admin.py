from django.contrib import admin
from track.models import (
    Tenant,
    Organisation,
    PurchaseOrderHeader,
    BusinessPartner
)

admin.site.register(Tenant)
admin.site.register(Organisation)
admin.site.register(PurchaseOrderHeader)
admin.site.register(BusinessPartner)
