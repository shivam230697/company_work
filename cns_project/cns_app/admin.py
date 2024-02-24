from django.contrib import admin
from .models import RawMaterialModel, ProductionModel, InvoiceModel, Customer, User, UserProfile, PaymentModel

# Register your models here.
admin.site.register(RawMaterialModel)
admin.site.register(ProductionModel)
admin.site.register(InvoiceModel)
admin.site.register(Customer)
admin.site.register(PaymentModel)

