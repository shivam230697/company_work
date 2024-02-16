from django.contrib import admin
from .models import RawMaterialModel, ProductionModel, FinalGoods

# Register your models here.
admin.site.register(RawMaterialModel)
admin.site.register(ProductionModel)
admin.site.register(FinalGoods)