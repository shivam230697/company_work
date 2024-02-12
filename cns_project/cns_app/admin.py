from django.contrib import admin
from .models import RawMaterialModel, ProductionModel

# Register your models here.
admin.site.register(RawMaterialModel)
admin.site.register(ProductionModel)