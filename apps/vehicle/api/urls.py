from django.urls import path
from apps.vehicle.api.views.general_views import (
    OwerListAPIView,
    VehicleUseListAPIView,
    AxesListAPIView,
    ManufacturerListAPIView,
    VehicleTypeListAPIView,
    FuelListAPIView
)
from apps.vehicle.api.views.vehicle_views import (
    TechnicalDataListCreateAPIView, 
    VehicleModelListCreateAPIView 
)

urlpatterns = [
    path('owner/',OwerListAPIView.as_view(),name = 'owerapiview'),
    path('vehicleuse/',VehicleUseListAPIView.as_view(),name = 'vehicleuseapiview'),
    path('axes/',AxesListAPIView.as_view(),name = 'axesapiview'),
    path('manufacturer/',ManufacturerListAPIView.as_view(),name = 'manufacturerapiview'),
    path('vehicletype/',VehicleTypeListAPIView.as_view(),name = 'vehicleuseapiview'),
    path('fuel/',FuelListAPIView.as_view(),name = 'fuelapiview'),
    path('technicaldata/',TechnicalDataListCreateAPIView.as_view(),name = 'technicaldataapiview'),
    path('vehiclemodel/',VehicleModelListCreateAPIView.as_view(),name = 'vehimcleodelapiview'),
]
