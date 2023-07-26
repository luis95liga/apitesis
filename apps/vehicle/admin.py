from django.contrib import admin
from apps.vehicle.models import *
# Register your models here.
admin.site.register(Owner)
admin.site.register(Vehicle)
admin.site.register(TechnicalData)
admin.site.register(Axes)
admin.site.register(Fuel)
admin.site.register(Manufacturer)
admin.site.register(VehicleModel)
admin.site.register(VehicleType)
admin.site.register(VehicleUse)
admin.site.register(GeneralData)
admin.site.register(MaintenamceCosts)
admin.site.register(DocumentType)
admin.site.register(DocumentVehicle)
admin.site.register(AssignTrailer)